# Kevin — AI Receptionist Dashboard

A single-file, responsive HTML dashboard for real-time operational visibility of calls, appointments, and system errors for an AI voice receptionist at Apex Construction Group.

## Features

- **Caller Insights**: Recent calls, repeat callers today, follow-up requests, VIP callers (5+ calls)
- **Today's Appointments**: Quick count, next appointment, detailed schedule table
- **Weekly Performance**: Call totals, conversion rate, week-over-week change
- **Call Volume Chart**: 7-day trend (line chart via Chart.js)
- **Conversion Funnel**: Total calls → Site visit intent → Scheduled appointments (bar chart)
- **Top Callers**: Top 5 by call count with last contact date
- **Tool Performance**: API/tool execution success rates (last 7 days, yellow alert if <95%)
- **Error Tracking**: Unresolved system errors with severity (critical=red, high=orange)
- **Auto-Refresh**: Updates every 30 seconds with timestamp
- **Responsive Design**: Mobile-friendly CSS Grid layout
- **Sample Data**: Built-in mock data for offline UI testing (toggle `useSampleData = true`)

## Tech Stack

- **Frontend**: Single-file HTML + inline CSS + vanilla JavaScript
- **API**: Supabase REST API (PostgREST)
- **Charts**: Chart.js (CDN: `https://cdn.jsdelivr.net/npm/chart.js`)
- **No build step**: Open `index.html` directly in browser or serve via HTTP

## Quick Start

### Option 1: Offline Testing (Sample Data)

```bash
# Just open in a browser
open [index.html](http://_vscodecontentref_/6)

# Or serve locally
python3 -m http.server 8080
# Visit http://localhost:8080/index.html
The dashboard loads with mock data by default. All widgets render without a database.

