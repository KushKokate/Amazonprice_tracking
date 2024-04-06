<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Amazon Price Tracking Script</h1>

<h2>DESCRIPTION : This Python script allows you to track prices of products on Amazon and receive email notifications when the prices drop below a specified threshold.</h2>

<h2>How It Works</h2>
    <p>The script fetches the webpage of the specified Amazon product using the requests library.
    It then parses the HTML content of the webpage using BeautifulSoup to extract the price of the product.
    If the price is found and exceeds the specified threshold, it sends an email notification using the smtplib library.</p>

<h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li>requests library</li>
        <li>bs4 (Beautiful Soup) library</li>
        <li>A Gmail account with less secure app access enabled or two-factor authentication with an app password.</li>
    </ul>

  <h2>Setup</h2>
    <ol>
        <li>Install the required libraries:</li>
        <pre><code>pip install requests beautifulsoup4</code></pre>
        <li>Update the <code>sender_mail</code>, <code>receiver_mail</code>, and <code>app_password</code> variables in the script with your Gmail credentials and the desired recipient email address.</li>
        <li>Replace the <code>url</code> variable with the URL of the Amazon product you want to track.</li>
        <li>Adjust the <code>headers</code> dictionary if necessary to match your browser's user-agent and preferred language.</li>
        <li>Run the script:</li>
        <pre><code>python amazon_price_tracker.py</code></pre>
    </ol>

  <h2>Note</h2>
    <ul>
        <li>Ensure that the specified Amazon product page structure matches the parsing logic in the script. If the structure changes, the script may need to be updated accordingly.</li>
        <li>This script is for educational purposes and personal use only. Be mindful of Amazon's Terms of Service and usage restrictions.</li>
    </ul>
</body>
</html>
