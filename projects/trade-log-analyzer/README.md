# Trade Log Analyzer

A simple Python project that analyzes trading-system results from a CSV trade log.

This project demonstrates how raw trade data can be converted into useful performance metrics.

## Files

| File                | Purpose                                          |
| ------------------- | ------------------------------------------------ |
| `analyze_trades.py` | Python script that reads and analyzes trade data |
| `sample_trades.csv` | Synthetic sample trade log used for testing      |

## What It Calculates

The analyzer calculates:

* Total trades
* Winning trades
* Losing trades
* Win rate
* Total net PnL
* Average win
* Average loss
* Best trade
* Worst trade
* Exit reason breakdown

## How to Run

Download or clone this repository, open this project folder, and run:

```bash
python analyze_trades.py
```

The script expects `sample_trades.csv` to be in the same folder.

## Example Output

```text
TRADE LOG ANALYZER REPORT
========================================
Total Trades:       8
Winning Trades:     5
Losing Trades:      3
Win Rate:           62.50%
Total Net PnL:      $37.20
Average Win:        $11.91
Average Loss:       $-7.45
Best Trade:         sample_003 ($18.40)
Worst Trade:        sample_002 ($-8.20)

EXIT REASON BREAKDOWN
========================================
TRAILING_STOP: 1 trades | Net PnL: $12.50
STOP_LOSS: 3 trades | Net PnL: $-22.35
TAKE_PROFIT: 2 trades | Net PnL: $33.00
ROE_LADDER: 1 trades | Net PnL: $9.75
TIME_STOP: 1 trades | Net PnL: $4.30
```

## Why This Project Matters

Trading systems generate raw logs, but raw logs are not enough.

A good analytics workflow should turn trade records into clear metrics that can be reviewed, compared, and improved over time.

## Skills Demonstrated

* Python
* CSV processing
* Data cleaning
* Performance metrics
* Trading analytics
* Report generation
