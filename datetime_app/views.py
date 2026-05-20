from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta

def time_calculator_view(request):
    # Get current time
    now = timezone.localtime(timezone.now())
    current_time_str = now.strftime('%A, %B %d, %Y <br> %H:%M:%S')
    
    offset_result_html = ""
    hours_input = request.GET.get('hours', '')
    
    # Process the form if submitted
    if hours_input:
        try:
            hours = float(hours_input)
            future_time = now + timedelta(hours=abs(hours))
            future_time_str = future_time.strftime('%A, %B %d, %Y <br> %H:%M:%S')
            
            past_time = now - timedelta(hours=abs(hours))
            past_time_str = past_time.strftime('%A, %B %d, %Y <br> %H:%M:%S')
            
            # Display result container
            offset_result_html = f"""
            <div class="result-box">
                <h2>Time {abs(hours):g} Hours in the Future</h2>
                <div class="time">{future_time_str}</div>
                <hr style="width: 50%;">
                <h2>Time {abs(hours):g} Hours in the Past</h2>
                <div class="time">{past_time_str}</div>
            </div>
            """
        except ValueError:
            offset_result_html = f"<div class='error'>Invalid input. Please enter a valid number indicating the hours.</div>"

    # Define the simple UI
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dynamic Time Calculator</title>
    </head>
    <body style="background-color: lightyellow;">
        <center>
            <h1 style="color: red;">Current Server Time</h1>
            
            <p style="font-size: 20px;"><b>{current_time_str}</b></p>
            <hr>
            
            <p>Calculate past and future time simultaneously:</p>
            
            <form method="GET" action="/">
                <label>Hours:</label>
                <input type="number" name="hours" step="any" value="{hours_input}" required>
                <br><br>
                <button type="submit">Calculate Time</button>
            </form>
            <br>
            <i>Enter a number of hours to see both the past and future times.</i>
            <br><br>
            <hr>
            
            {offset_result_html}
        </center>
    </body>
    </html>
    """
    return HttpResponse(html)
