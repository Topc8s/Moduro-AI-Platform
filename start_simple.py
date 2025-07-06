#!/usr/bin/env python3
"""
Moduro AI Platform - Simple Startup Script
Free AI Development Platform
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("🔧 Installing requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements_simple.txt"])
        print("✅ Requirements installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements")
        return False
    return True

def start_server():
    """Start the Flask server"""
    print("🚀 Starting Moduro AI Platform...")
    print("📊 Features:")
    print("   • Data Analysis & Expansion")
    print("   • Python Code Analysis & Enhancement")
    print("   • AI Chat Assistant")
    print("   • Real-time Metrics")
    print("   • Free & Self-contained")
    print()
    print("🌐 Server will be available at: http://localhost:5000")
    print("📱 HTML Interface: http://localhost:5000")
    print("🔌 API Endpoints: http://localhost:5000/api/*")
    print()
    print("Press Ctrl+C to stop the server")
    print()
    
    try:
        subprocess.run([sys.executable, "simple_api.py"])
    except KeyboardInterrupt:
        print("\n👋 Server stopped")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

def main():
    """Main startup function"""
    print("🚀 Moduro AI Platform - Simple Version")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("simple_api.py"):
        print("❌ Error: simple_api.py not found")
        print("Please run this script from the Moduro directory")
        return
    
    # Install requirements
    if not install_requirements():
        return
    
    # Start server
    start_server()

if __name__ == "__main__":
    main() 