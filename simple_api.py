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
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
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

logger.info("Moduro Simple API starting up")

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.route('/api/upload', methods=['POST'])
def upload_data():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Simulate data processing
        sample_data = [
            {'id': 1, 'name': 'Sample 1', 'value': 100},
            {'id': 2, 'name': 'Sample 2', 'value': 200},
            {'id': 3, 'name': 'Sample 3', 'value': 300}
        ]
        
        global data_store
        data_store = sample_data
        
        return jsonify({
            'data': sample_data,
            'records': len(sample_data),
            'message': 'Data uploaded successfully'
        })
        
    except Exception as e:
        logger.error(f"Upload error: {str(e)}")
        return jsonify({'error': 'Upload failed'}), 500

@app.route('/api/analyze', methods=['POST'])
def analyze_data():
    try:
        global data_store, analysis_results
        
        if not data_store:
            return jsonify({
                'analysis': {
                    'total_records': 0,
                    'patterns': [],
                    'insights': ['No data available for analysis'],
                    'recommendations': ['Upload data to begin analysis']
                }
            })
        
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
        return jsonify({'analysis': analysis})
        
    except Exception as e:
        logger.error(f"Analysis error: {str(e)}")
        return jsonify({'error': 'Analysis failed'}), 500

@app.route('/api/expand', methods=['POST'])
def expand_data():
    try:
        global data_store, expansion_results
        
        if not data_store:
            return jsonify({
                'expansion': {
                    'data': [],
                    'new_features': 0,
                    'expanded_count': 0
                }
            })
        
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
        return jsonify({'expansion': expansion})
        
    except Exception as e:
        logger.error(f"Expansion error: {str(e)}")
        return jsonify({'error': 'Expansion failed'}), 500

@app.route('/api/analyze-python', methods=['POST'])
def analyze_python_code():
    try:
        data = request.get_json()
        code = data.get('code', '')
        
        if not code.strip():
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
        except SyntaxError as e:
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
        modular_score = min(100, max(0, 100 - complexity * 10))
        
        analysis = {
            'complexity': complexity,
            'functions': functions,
            'classes': classes,
            'imports': imports,
            'modular_score': modular_score,
            'suggestions': [
                f'Found {len(functions)} functions and {len(classes)} classes',
                f'Code complexity score: {complexity}',
                'Consider adding docstrings for better documentation',
                'Use type hints to improve code clarity'
            ]
        }
        
        global code_analysis_results
        code_analysis_results = analysis
        
        return jsonify({'analysis': analysis})
        
    except Exception as e:
        logger.error(f"Code analysis error: {str(e)}")
        return jsonify({'error': 'Code analysis failed'}), 500

@app.route('/api/expand-python', methods=['POST'])
def expand_python_code():
    try:
        data = request.get_json()
        code = data.get('code', '')
        
        if not code.strip():
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
        
        return jsonify({
            'expanded_code': expanded_code,
            'metrics': expansion_metrics
        })
        
    except Exception as e:
        logger.error(f"Code expansion error: {str(e)}")
        return jsonify({'error': 'Code expansion failed'}), 500

@app.route('/api/modules')
def get_modules():
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
        
        return jsonify({'modules': modules})
        
    except Exception as e:
        logger.error(f"Modules error: {str(e)}")
        return jsonify({'error': 'Failed to get modules'}), 500

@app.route('/api/execute', methods=['POST'])
def execute_function():
    try:
        data = request.get_json()
        function_name = data.get('function', '')
        params = data.get('params', {})
        
        # Simulate function execution
        result = {
            'function': function_name,
            'status': 'success',
            'message': f'Function {function_name} executed successfully',
            'result': f'Simulated result for {function_name}',
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(result)
        
    except Exception as e:
        logger.error(f"Function execution error: {str(e)}")
        return jsonify({'error': 'Function execution failed'}), 500

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get('message', '')
        
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
        
        return jsonify({'response': response})
        
    except Exception as e:
        logger.error(f"Chat error: {str(e)}")
        return jsonify({'error': 'Chat failed'}), 500

@app.route('/api/metrics')
def get_metrics():
    try:
        global metrics
        return jsonify(metrics)
        
    except Exception as e:
        logger.error(f"Metrics error: {str(e)}")
        return jsonify({'error': 'Failed to get metrics'}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"500 error: {str(error)}")
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    logger.info("Starting Moduro Simple API")
    logger.info("Server will be available at http://localhost:5000")
    logger.info("HTML interface available at http://localhost:5000")
    
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}") 