'''title: Iris Classification
order_name: 001 iris
'''

import simplestart as ss
import os

ss.config.title = "Iris Classification"

# Create sidebar navigation
left_sidebar = ss.sidebar(position="left")
with left_sidebar:
    ss.md("# Iris Classification")
    ss.space("mb-4")
    ss.write("A Machine Learning Application Example Based on SimpleStart")

# Main content
ss.anchor_point("main-content")
ss.md("## Welcome to Iris Classification App")
ss.write("This is a machine learning application example based on the SimpleStart framework, demonstrating how to build a complete machine learning workflow using SimpleStart.")
ss.write("Please browse through the various functional modules using the left navigation bar.")

# Display cover image
ss.space("mb-8")
ss.image(
    src="./data/illustration.png",
    width="800px",
    alt="Gemini_Generated_Image"
)
ss.space("mb-4")
ss.text("Gemini Generated Image", tag = "b")