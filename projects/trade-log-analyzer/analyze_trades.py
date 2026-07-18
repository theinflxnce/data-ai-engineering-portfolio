import csv
from pathlib import Path


def load_trades(file_path):
    """Load trade data from a CSV file."""
    trades = []

    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["net_pnl_usdt"] = float(row["net_pnl_usdt"])
            row["trade_duration_min"] = float(row["trade_duration_min"])
            row["roe_peak_pct"] = float(row["roe_peak_pct"])
            row["roe_exit_pct"] = float(row["roe_exit_pct"])
            trades.append(row)

    return trades


def calculate_summary(trades):
    """Calculate basic trading performance metrics."""
    total_trades = len(trades)

    if total_trades == 0:
        return {}

    winning_trades = [trade for trade in trades if trade["net_pnl_usdt"] > 0]
    losing_trades = [trade for trade in trades if trade["net_pnl_usdt"] <= 0]

    total_pnl = sum(trade["net_pnl_usdt"] for trade in trades)
    win_rate = len(winning_trades) / total_trades * 100

    average_win = (
        sum(trade["net_pnl_usdt"] for trade in winning_trades) / len(winning_trades)
        if winning_trades
        else 0
    )

    average_loss = (
        sum(trade["net_pnl_usdt"] for trade in losing_trades) / len(losing_trades)
        if losing_trades
        else 0
    )

    best_trade = max(trades, key=lambda trade: trade["net_pnl_usdt"])
    worst_trade = min(trades, key=lambda trade: trade["net_pnl_usdt"])

    return {
        "total_trades": total_trades,
        "winning_trades": len(winning_trades),
        "losing_trades": len(losing_trades),
        "win_rate_pct": win_rate,
        "total_pnl_usdt": total_pnl,
        "average_win_usdt": average_win,
        "average_loss_usdt": average_loss,
        "best_trade_id": best_trade["trade_id"],
        "best_trade_pnl": best_trade["net_pnl_usdt"],
        "worst_trade_id": worst_trade["trade_id"],
        "worst_trade_pnl": worst_trade["net_pnl_usdt"],
    }


def exit_reason_breakdown(trades):
    """Group trades by exit reason."""
    breakdown = {}

    for trade in trades:
        reason = trade["exit_reason"]

        if reason not in breakdown:
            breakdown[reason] = {
                "count": 0,
                "net_pnl_usdt": 0,
            }

        breakdown[reason]["count"] += 1
        breakdown[reason]["net_pnl_usdt"] += trade["net_pnl_usdt"]

    return breakdown


def print_report(summary, breakdown):
    """Print a clean report in the terminal."""
    print("\nTRADE LOG ANALYZER REPORT")
    print("=" * 40)

    print(f"Total Trades:       {summary['total_trades']}")
    print(f"Winning Trades:     {summary['winning_trades']}")
    print(f"Losing Trades:      {summary['losing_trades']}")
    print(f"Win Rate:           {summary['win_rate_pct']:.2f}%")
    print(f"Total Net PnL:      ${summary['total_pnl_usdt']:.2f}")
    print(f"Average Win:        ${summary['average_win_usdt']:.2f}")
    print(f"Average Loss:       ${summary['average_loss_usdt']:.2f}")
    print(f"Best Trade:         {summary['best_trade_id']} (${summary['best_trade_pnl']:.2f})")
    print(f"Worst Trade:        {summary['worst_trade_id']} (${summary['worst_trade_pnl']:.2f})")

    print("\nEXIT REASON BREAKDOWN")
    print("=" * 40)

    for reason, values in breakdown.items():
        print(f"{reason}: {values['count']} trades | Net PnL: ${values['net_pnl_usdt']:.2f}")


def main():
    file_path = Path("sample_trades.csv")

    if not file_path.exists():
        print("Error: sample_trades.csv not found.")
        print("Place the CSV file in the same folder as this script.")
        return

    trades = load_trades(file_path)
    summary = calculate_summary(trades)
    breakdown = exit_reason_breakdown(trades)

    print_report(summary, breakdown)


if __name__ == "__main__":
    main()
