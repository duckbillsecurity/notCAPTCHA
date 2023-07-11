# notCAPTCHA

A Python script to generate a notCAPTCHA HTML file with embedded SVG image and obfuscated URL.

## Description

`notCAPTCHA` is a Python script that generates an HTML file with a simple CAPTCHA-like checkbox. When the checkbox is clicked, it opens a URL provided as a command-line argument. The SVG image and URL are embedded in the HTML file using base64 encoding with additional obfuscation.

## Requirements

- Python 3.x

## Usage

`
python notCAPTCHA.py <URL> <SVG_file>
`

Replace `<URL>` with the URL you want to open when the checkbox is clicked, and `<SVG_file>` with the path to the SVG image file.

The script will generate an HTML file named `notCAPTCHA.html` in the current directory.

## Example

`
python notCAPTCHA.py https://example.com RecaptchaLogo.svg
`

This will generate an HTML file with a checkbox and an embedded SVG image based on `RecaptchaLogo.svg`. Clicking the checkbox will open `https://example.com`.
