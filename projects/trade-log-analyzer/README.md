# Trade Log Analyzer

This project is a Python-based data analysis tool for reviewing trading-system results from CSV trade logs.

The goal is to turn raw trade data into useful performance insights.

## Project Purpose

Trading systems produce a lot of raw trade data.

A trade log analyzer helps convert that raw data into clear metrics such as win rate, net profit and loss, average winner, average loser, and exit reason breakdown.

## What This Project Shows

This project demonstrates practical data analytics skills using trading data.

It focuses on:

* Reading CSV files
* Cleaning trade data
* Calculating performance metrics
* Grouping trades by result and exit reason
* Summarizing trading performance
* Preparing data for reporting

## Planned Metrics

The analyzer will calculate:

* Total trades
* Winning trades
* Losing trades
* Win rate
* Net PnL
* Average win
* Average loss
* Best trade
* Worst trade
* Exit reason breakdown

## Sample Input

The tool uses a sanitized sample trade log with columns such as:

* trade_id
* market
* side
* entry_time
* exit_time
* entry_price
* exit_price
* trade_duration_min
* exit_reason
* roe_peak_pct
* roe_exit_pct
* net_pnl_usdt
* result

## Why This Matters

This project connects trading-system development with data analytics.

Instead of only showing trading results, it shows how raw trade data can be processed, reviewed, and turned into better decisions.

## Skills Demonstrated

* Python
* CSV analysis
* Data cleaning
* Metric calculation
* Performance reporting
* Trading analytics
