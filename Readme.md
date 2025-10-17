<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculator CLI App - README</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 40px 20px;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            overflow: hidden;
        }

        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 60px 40px;
            text-align: center;
        }

        .header h1 {
            font-size: 3em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }

        .header p {
            font-size: 1.2em;
            opacity: 0.95;
        }

        .content {
            padding: 60px 40px;
        }

        .section {
            margin-bottom: 50px;
        }

        .section h2 {
            font-size: 1.8em;
            color: #667eea;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .section h2::before {
            content: '📋';
            font-size: 1.5em;
        }

        .section.features h2::before { content: '✨'; }
        .section.tools h2::before { content: '🛠️'; }
        .section.guide h2::before { content: '📖'; }
        .section.setup h2::before { content: '⚙️'; }
        .section.usage h2::before { content: '▶️'; }

        .objective-box {
            background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
            padding: 25px;
            border-left: 5px solid #667eea;
            border-radius: 10px;
            margin-bottom: 30px;
            font-size: 1.1em;
            color: #333;
        }

        .features-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 30px;
        }

        .feature-card {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 12px;
            border-left: 4px solid #667eea;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(102, 126, 234, 0.1);
        }

        .feature-card strong {
            color: #667eea;
            font-size: 1.05em;
        }

        .tools-list {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-bottom: 30px;
        }

        .tool-item {
            background: #f0f4ff;
            padding: 15px 20px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            gap: 12px;
            font-weight: 500;
            color: #667eea;
        }

        .tool-item::before {
            content: '✓';
            background: #667eea;
            color: white;
            width: 24px;
            height: 24px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }

        .guide-steps {
            counter-reset: step;
            list-style: none;
        }

        .guide-steps li {
            counter-increment: step;
            margin-bottom: 20px;
            padding-left: 50px;
            position: relative;
            font-size: 1.05em;
            color: #333;
            line-height: 1.6;
        }

        .guide-steps li::before {
            content: counter(step);
            position: absolute;
            left: 0;
            top: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 1.1em;
        }

        .setup-box {
            background: #1a1a2e;
            color: #00ff88;
            padding: 25px;
            border-radius: 12px;
            font-family: 'Courier New', monospace;
            overflow-x: auto;
            margin-bottom: 20px;
        }

        .setup-box code {
            font-size: 1.05em;
            line-height: 1.8;
        }

        .code-line {
            display: block;
            margin-bottom: 8px;
        }

        .outcome-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            margin-top: 40px;
            font-size: 1.3em;
            font-weight: 600;
        }

        .operations-showcase {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            margin-bottom: 30px;
        }

        @media (max-width: 768px) {
            .operations-showcase {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .features-grid, .tools-list {
                grid-template-columns: 1fr;
            }

            .header h1 {
                font-size: 2em;
            }

            .content {
                padding: 30px 20px;
            }
        }

        .operation-badge {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-weight: bold;
            font-size: 1.3em;
            transition: transform 0.3s ease;
        }

        .operation-badge:hover {
            transform: scale(1.05);
        }

        .footer {
            background: #f8f9fa;
            padding: 30px 40px;
            text-align: center;
            color: #666;
            border-top: 1px solid #e0e0e0;
        }

        .highlight {
            background: #fff3cd;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 600;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🧮 Calculator CLI App</h1>
            <p>A Command-Line Calculator Supporting Basic Operations</p>
        </div>

        <div class="content">
            <!-- Objective Section -->
            <div class="section">
                <h2>Objective</h2>
                <div class="objective-box">
                    Create a command-line calculator supporting basic arithmetic operations with a user-friendly interface and robust error handling.
                </div>
            </div>

            <!-- Operations Showcase -->
            <div class="section features">
                <h2>Supported Operations</h2>
                <div class="operations-showcase">
                    <div class="operation-badge">➕ Addition</div>
                    <div class="operation-badge">➖ Subtraction</div>
                    <div class="operation-badge">✖️ Multiplication</div>
                    <div class="operation-badge">➗ Division</div>
                </div>
            </div>

            <!-- Tools Section -->
            <div class="section tools">
                <h2>Tools & Technologies</h2>
                <div class="tools-list">
                    <div class="tool-item">Python 3.x</div>
                    <div class="tool-item">VS Code / Text Editor</div>
                    <div class="tool-item">Terminal / Command Prompt</div>
                    <div class="tool-item">Git (Optional)</div>
                </div>
                <p style="color: #666; margin-top: 15px;"><strong>Deliverable:</strong> A Python script named <span class="highlight">calculator.py</span></p>
            </div>

            <!-- Features Section -->
            <div class="section features">
                <h2>Key Features</h2>
                <div class="features-grid">
                    <div class="feature-card">
                        <strong>Functions for Operations</strong><br>
                        Separate functions for add, subtract, multiply, and divide
                    </div>
                    <div class="feature-card">
                        <strong>User Input Handling</strong><br>
                        Interactive input() method for seamless user interaction
                    </div>
                    <div class="feature-card">
                        <strong>Continuous Loop</strong><br>
                        Runs until user chooses to exit the application
                    </div>
                    <div class="feature-card">
                        <strong>Error Handling</strong><br>
                        Validates input and prevents division by zero errors
                    </div>
                </div>
            </div>

            <!-- Guide Section -->
            <div class="section guide">
                <h2>Implementation Guide</h2>
                <ol class="guide-steps">
                    <li><strong>Create operation functions</strong> - Define separate functions for addition, subtraction, multiplication, and division operations</li>
                    <li><strong>Implement user input</strong> - Use input() function to get two numbers and operation choice from the user</li>
                    <li><strong>Build main loop</strong> - Create a while loop that continues until the user selects the exit option</li>
                    <li><strong>Add error handling</strong> - Validate inputs and handle edge cases like division by zero</li>
                    <li><strong>Create menu display</strong> - Show clear options for users to select operations</li>
                </ol>
            </div>

            <!-- Setup Section -->
            <div class="section setup">
                <h2>Setup & Installation</h2>
                <div class="setup-box">
                    <code>
                        <span class="code-line"># 1. Save the calculator code as calculator.py</span>
                        <span class="code-line"></span>
                        <span class="code-line"># 2. Open terminal/command prompt</span>
                        <span class="code-line"></span>
                        <span class="code-line"># 3. Navigate to the file directory</span>
                        <span class="code-line">$ cd /path/to/calculator</span>
                        <span class="code-line"></span>
                        <span class="code-line"># 4. Run the calculator</span>
                        <span class="code-line">$ python calculator.py</span>
                    </code>
                </div>
            </div>

            <!-- Usage Section -->
            <div class="section usage">
                <h2>How to Use</h2>
                <ol class="guide-steps">
                    <li>Run the calculator script from terminal: <span class="highlight">python calculator.py</span></li>
                    <li>The menu will display available operations (1-4) and exit option (5)</li>
                    <li>Select an operation by entering the corresponding number</li>
                    <li>Enter two numbers when prompted</li>
                    <li>View the calculation result</li>
                    <li>Press 5 to exit or continue with more calculations</li>
                </ol>
            </div>

            <!-- Outcome Section -->
            <div class="outcome-box">
                ✅ Outcome: A Well-Structured, Professional-Grade CLI Application
            </div>
        </div>

        <div class="footer">
            <p>📝 Task 1: Build a Calculator CLI App | Created with ❤️</p>
            <p style="font-size: 0.9em; margin-top: 10px;">Ready to deploy and fully functional</p>
        </div>
    </div>
</body>
</html>