from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import json
import ast
import logging
from datetime import datetime
import traceback

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('moduro.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Global data storage
data_store = []
analysis_results = {}
expansion_results = {}
code_analysis_results = {}
code_expansion_results = {}
metrics = {
    'total_lines': 0,
    'total_chars': 0,
    'expansions': 0
}

logger.info("Moduro Flask application starting up")
logger.info("Initializing data stores and metrics")

@app.route('/')
def index():
    logger.info("Serving index page")
    return send_from_directory('frontend/build', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    logger.info(f"Serving static file: {path}")
    return send_from_directory('frontend/build', path)

@app.route('/api/health')
def health_check():
    logger.info("Health check requested")
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.route('/api/upload', methods=['POST'])
def upload_data():
    logger.info("Data upload requested")
    try:
        if 'file' not in request.files:
            logger.warning("No file in upload request")
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            logger.warning("Empty filename in upload")
            return jsonify({'error': 'No file selected'}), 400
        
        logger.info(f"Processing file: {file.filename}")
        
        # Simulate data processing
        sample_data = [
            {'id': 1, 'name': 'Sample 1', 'value': 100},
            {'id': 2, 'name': 'Sample 2', 'value': 200},
            {'id': 3, 'name': 'Sample 3', 'value': 300}
        ]
        
        global data_store
        data_store = sample_data
        
        logger.info(f"Upload successful, {len(sample_data)} records processed")
        
        return jsonify({
            'data': sample_data,
            'records': len(sample_data),
            'message': 'Data uploaded successfully'
        })
        
    except Exception as e:
        logger.error(f"Upload error: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        return jsonify({'error': 'Upload failed'}), 500

@app.route('/api/analyze', methods=['POST'])
def analyze_data():
    logger.info("Data analysis requested")
    try:
        global data_store, analysis_results
        
        if not data_store:
            logger.warning("No data available for analysis")
            return jsonify({
                'analysis': {
                    'total_records': 0,
                    'patterns': [],
                    'insights': ['No data available for analysis'],
                    'recommendations': ['Upload data to begin analysis']
                }
            })
        
        logger.info(f"Analyzing {len(data_store)} records")
        
        # Simulate AI analysis
        analysis = {
            'total_records': len(data_store),
            'patterns': [
                {'type': 'numeric', 'field': 'value', 'trend': 'increasing'},
                {'type': 'categorical', 'field': 'name', 'unique_values': 3}
            ],
            'insights': [
                'Data shows consistent value progression',
                'All records have unique identifiers',
                'Numeric values range from 100 to 300'
            ],
            'recommendations': [
                'Consider adding more diverse data points',
                'Implement data validation for numeric fields',
                'Add timestamp tracking for temporal analysis'
            ]
        }
        
        analysis_results = analysis
        logger.info("Analysis completed successfully")
        
        return jsonify({'analysis': analysis})
        
    except Exception as e:
        logger.error(f"Analysis error: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        return jsonify({'error': 'Analysis failed'}), 500

@app.route('/api/expand', methods=['POST'])
def expand_data():
    logger.info("Data expansion requested")
    try:
        global data_store, expansion_results
        
        if not data_store:
            logger.warning("No data available for expansion")
            return jsonify({
                'expansion': {
                    'data': [],
                    'new_features': 0,
                    'expanded_count': 0
                }
            })
        
        logger.info(f"Expanding {len(data_store)} records")
        
        # Simulate AI expansion
        expanded_data = []
        for i, record in enumerate(data_store):
            expanded_record = {
                **record,
                'category': f'Category_{i % 3 + 1}',
                'score': record['value'] * 0.1,
                'status': 'active' if record['value'] > 150 else 'pending'
            }
            expanded_data.append(expanded_record)
        
        expansion = {
            'data': expanded_data,
            'new_features': 3,
            'expanded_count': len(expanded_data)
        }
        
        expansion_results = expansion
        logger.info(f"Expansion completed: {len(expanded_data)} records, {expansion['new_features']} new features")
        
        return jsonify({'expansion': expansion})
        
    except Exception as e:
        logger.error(f"Expansion error: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        return jsonify({'error': 'Expansion failed'}), 500

@app.route('/api/analyze-python', methods=['POST'])
def analyze_python_code():
    logger.info("Python code analysis requested")
    try:
        data = request.get_json()
        code = data.get('code', '')
        
        logger.info(f"Analyzing code ({len(code)} characters)")
        
        if not code.strip():
            logger.warning("Empty code provided for analysis")
            return jsonify({
                'analysis': {
                    'complexity': 0,
                    'functions': [],
                    'classes': [],
                    'imports': [],
                    'suggestions': ['Please provide code to analyze']
                }
            })
        
        # Parse Python code
        try:
            tree = ast.parse(code)
            logger.info("Code parsed successfully")
        except SyntaxError as e:
            logger.warning(f"Syntax error in code: {str(e)}")
            return jsonify({
                'analysis': {
                    'complexity': 0,
                    'functions': [],
                    'classes': [],
                    'imports': [],
                    'suggestions': [f'Syntax error: {str(e)}']
                }
            })
        
        # Analyze code structure
        functions = []
        classes = []
        imports = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions.append({
                    'name': node.name,
                    'args': len(node.args.args),
                    'lineno': node.lineno
                })
            elif isinstance(node, ast.ClassDef):
                classes.append({
                    'name': node.name,
                    'methods': len([n for n in node.body if isinstance(n, ast.FunctionDef)]),
                    'lineno': node.lineno
                })
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ''
                for alias in node.names:
                    imports.append(f"{module}.{alias.name}")
        
        complexity = len(functions) + len(classes) * 2
        
        analysis = {
            'complexity': complexity,
            'functions': functions,
            'classes': classes,
            'imports': imports,
            'suggestions': [
                f'Found {len(functions)} functions and {len(classes)} classes',
                f'Code complexity score: {complexity}',
                'Consider adding docstrings for better documentation',
                'Use type hints to improve code clarity'
            ]
        }
        
        global code_analysis_results
        code_analysis_results = analysis
        
        logger.info(f"Code analysis completed: {len(functions)} functions, {len(classes)} classes, complexity {complexity}")
        
        return jsonify({'analysis': analysis})
        
    except Exception as e:
        logger.error(f"Code analysis error: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        return jsonify({'error': 'Code analysis failed'}), 500

@app.route('/api/expand-python', methods=['POST'])
def expand_python_code():
    logger.info("Python code expansion requested")
    try:
        data = request.get_json()
        code = data.get('code', '')
        
        logger.info(f"Expanding code ({len(code)} characters)")
        
        if not code.strip():
            logger.warning("Empty code provided for expansion")
            return jsonify({
                'expanded_code': '',
                'metrics': {
                    'original_lines': 0,
                    'original_chars': 0,
                    'new_lines': 0,
                    'new_chars': 0,
                    'total_lines': 0,
                    'total_chars': 0,
                    'expansion_rate': 0
                }
            })
        
        # Simulate AI code expansion
        original_lines = len(code.split('\n'))
        original_chars = len(code)
        
        # Add documentation, error handling, and type hints
        expanded_code = f'''"""
Enhanced version of the provided code with additional features.
Generated by Moduro AI Platform.
"""

{code}

# Additional utility functions
def validate_input(data):
    """Validate input data."""
    if not data:
        raise ValueError("Data cannot be empty")
    return True

def process_result(result):
    """Process and format the result."""
    if isinstance(result, (list, tuple)):
        return [str(item) for item in result]
    return str(result)

# Error handling wrapper
def safe_execute(func, *args, **kwargs):
    """Safely execute a function with error handling."""
    try:
        return func(*args, **kwargs)
    except Exception as exc:
        print(f"Error executing {{func.__name__}}: {{exc}}")
        return None
'''
        
        new_lines = len(expanded_code.split('\n')) - original_lines
        new_chars = len(expanded_code) - original_chars
        total_lines = original_lines + new_lines
        total_chars = original_chars + new_chars
        expansion_rate = (new_chars / original_chars * 100) if original_chars > 0 else 0
        
        expansion_metrics = {
            'original_lines': original_lines,
            'original_chars': original_chars,
            'new_lines': new_lines,
            'new_chars': new_chars,
            'total_lines': total_lines,
            'total_chars': total_chars,
            'expansion_rate': round(expansion_rate, 2)
        }
        
        global code_expansion_results, metrics
        code_expansion_results = expanded_code
        metrics['total_lines'] += total_lines
        metrics['total_chars'] += total_chars
        metrics['expansions'] += 1
        
        logger.info(f"Code expansion completed: +{new_lines} lines, +{new_chars} chars, {expansion_rate:.1f}% expansion")
        
        return jsonify({
            'expanded_code': expanded_code,
            'metrics': expansion_metrics
        })
        
    except Exception as e:
        logger.error(f"Code expansion error: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        return jsonify({'error': 'Code expansion failed'}), 500

@app.route('/api/modules')
def get_modules():
    logger.info("Modules request")
    try:
        modules = [
            {
                'name': 'data_expansion',
                'description': 'AI-driven data analysis and expansion',
                'status': 'active',
                'functions': ['expand_data', 'analyze_data']
            },
            {
                'name': 'code_analysis',
                'description': 'Python code analysis and enhancement',
                'status': 'active',
                'functions': ['analyze_python', 'expand_python']
            }
        ]
        
        logger.info(f"Returning {len(modules)} modules")
        return jsonify({'modules': modules})
        
    except Exception as e:
        logger.error(f"Modules error: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        return jsonify({'error': 'Failed to get modules'}), 500

@app.route('/api/execute', methods=['POST'])
def execute_function():
    logger.info("Function execution requested")
    try:
        data = request.get_json()
        function_name = data.get('function', '')
        params = data.get('params', {})
        
        logger.info(f"Executing function: {function_name} with params: {params}")
        
        # Simulate function execution
        result = {
            'function': function_name,
            'status': 'success',
            'message': f'Function {function_name} executed successfully',
            'result': f'Simulated result for {function_name}',
            'timestamp': datetime.now().isoformat()
        }
        
        logger.info(f"Function {function_name} executed successfully")
        
        return jsonify(result)
        
    except Exception as e:
        logger.error(f"Function execution error: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        return jsonify({'error': 'Function execution failed'}), 500

@app.route('/api/chat', methods=['POST'])
def chat():
    logger.info("Chat message received")
    try:
        data = request.get_json()
        message = data.get('message', '')
        
        logger.info(f"Processing chat message: {message[:50]}...")
        
        # Simulate AI response
        responses = [
            "I'm here to help you with data analysis and code expansion!",
            "You can upload data for analysis or write Python code for enhancement.",
            "The platform supports both data expansion and code analysis features.",
            "Try uploading some data or writing code to see the AI in action!",
            "I can help analyze your data patterns and suggest improvements."
        ]
        
        import random
        response = random.choice(responses)
        
        logger.info(f"AI response: {response}")
        
        return jsonify({'response': response})
        
    except Exception as e:
        logger.error(f"Chat error: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        return jsonify({'error': 'Chat failed'}), 500

@app.route('/api/metrics')
def get_metrics():
    logger.info("Metrics request")
    try:
        global metrics
        logger.info(f"Returning metrics: {metrics}")
        return jsonify(metrics)
        
    except Exception as e:
        logger.error(f"Metrics error: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        return jsonify({'error': 'Failed to get metrics'}), 500

@app.errorhandler(404)
def not_found(error):
    logger.warning(f"404 error: {request.url}")
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"500 error: {str(error)}")
    logger.error(f"Traceback: {traceback.format_exc()}")
    return jsonify({'error': 'Internal server error'}), 500

# --- Ollama Multi-Model LLM Endpoints ---
import requests

OLLAMA_URL = "http://localhost:11434"

@app.route('/api/models')
def list_models():
    try:
        resp = requests.get(f"{OLLAMA_URL}/api/tags")
        models = [m['name'] for m in resp.json().get('models', [])]
        return jsonify({'models': models})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/compare', methods=['POST'])
def compare_models():
    data = request.json
    if data is None:
        return jsonify({'error': 'Invalid JSON data'}), 400
    
    prompt = data.get('prompt', '')
    models = data.get('models', ['deepseek-coder:7b'])
    results = {}
    for model in models:
        try:
            resp = requests.post(f"{OLLAMA_URL}/api/generate", json={
                "model": model,
                "prompt": prompt,
                "stream": False
            })
            response = resp.json().get('response', '')
            results[model] = response
        except Exception as e:
            results[model] = f"Error: {str(e)}"
    return jsonify({'results': results})

if __name__ == '__main__':
    logger.info("Starting Moduro Flask application")
    logger.info("Server will be available at http://localhost:5000")
    logger.info("Serving static files from frontend/build")
    logger.info("Debug mode enabled")
    
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}") 