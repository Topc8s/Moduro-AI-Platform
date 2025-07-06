# Moduro AI Platform

A **completely free, self-contained AI-driven modular development platform** inspired by Replit, designed for Proxmox and AI automation. No API keys, no external dependencies, no signups required.

## 🌟 Features

### 🎯 **3 Main Tabs with Comprehensive Functionality**

#### 1. **Data Analysis Tab**
- **Drag & Drop File Upload** - Support for JSON, CSV, and text files
- **Real-time Data Analysis** - Structure analysis, pattern recognition, insights generation
- **Data Expansion** - AI-driven feature generation and data enhancement
- **Interactive Statistics** - Visual data metrics and type analysis
- **Export Capabilities** - Download processed and expanded data

#### 2. **Code Editor Tab**
- **Python Code Analysis** - AST-based code structure analysis
- **Modularity Scoring** - Function and class detection with quality metrics
- **Code Expansion** - AI-powered code enhancement with error handling
- **Real-time Metrics** - Lines of code, complexity, and improvement suggestions
- **Syntax Highlighting** - Beautiful dark theme code editor

#### 3. **AI Assistant Tab**
- **Context-Aware Chat** - AI responses based on current platform state
- **Quick Actions** - One-click data analysis, code review, and expansion
- **Platform Integration** - Seamless communication with all tabs
- **Real-time Statistics** - Live platform metrics and function results
- **Smart Suggestions** - AI-powered recommendations and insights

### 🎨 **Dark Space Theme**
- **Electric Purple** (#8B5CF6) primary color
- **Neon Pink** (#EC4899) secondary accents
- **Space-like Gradients** and glowing effects
- **Responsive Design** with Material-UI components
- **Accessibility** compliant with ARIA labels

### 🔧 **Free & Self-Contained**
- **No API Keys Required** - All processing done locally
- **No External Dependencies** - No OpenAI, no paid services
- **No Signups** - Works immediately out of the box
- **Offline Capable** - Full functionality without internet
- **Privacy First** - All data stays on your machine

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd Moduro
```

2. **Install backend dependencies**
```bash
pip install -r requirements.txt
```

3. **Install frontend dependencies**
```bash
npm install --prefix frontend
```

4. **Start the backend server**
```bash
python app.py
```

5. **Start the frontend development server**
```bash
npm start --prefix frontend
```

6. **Open your browser**
Navigate to `http://localhost:3000`

## 🏗️ Architecture

### Backend (Flask)
```
app.py
├── FreeAISimulator class
│   ├── Data analysis & expansion
│   ├── Python code analysis
│   ├── Pattern recognition
│   └── AI response generation
├── RESTful API endpoints
│   ├── /api/upload - File upload
│   ├── /api/analyze - Data analysis
│   ├── /api/expand - Data expansion
│   ├── /api/analyze-python - Code analysis
│   ├── /api/expand-python - Code expansion
│   ├── /api/chat - AI chat
│   └── /api/metrics - Platform statistics
└── In-memory data storage
```

### Frontend (React)
```
frontend/src/
├── components/
│   ├── DataAnalysis.js - Data upload & analysis
│   ├── CodeEditor.js - Python code editor
│   └── AIAssistant.js - AI chat interface
├── context/
│   └── AppContext.js - Global state management
├── services/
│   └── functions.js - API communication
└── App.js - Main application with 3 tabs
```

## 📊 API Endpoints

### Data Processing
- `POST /api/upload` - Upload and parse data files
- `POST /api/analyze` - Analyze uploaded data structure
- `POST /api/expand` - Expand data with synthetic features

### Code Analysis
- `POST /api/analyze-python` - Analyze Python code structure
- `POST /api/expand-python` - Expand Python code with enhancements

### AI & Functions
- `POST /api/chat` - AI chat responses
- `POST /api/execute` - Execute platform functions
- `GET /api/modules` - Get available modules
- `GET /api/metrics` - Platform statistics

## 🎯 Usage Examples

### Data Analysis Workflow
1. **Upload Data** - Drag & drop JSON/CSV files
2. **Analyze Structure** - Get insights and patterns
3. **Expand Features** - Add synthetic data features
4. **Export Results** - Download enhanced dataset

### Code Development Workflow
1. **Write Python Code** - Use the integrated editor
2. **Analyze Structure** - Get modularity scores and suggestions
3. **Expand Code** - Add error handling and enhancements
4. **Review Metrics** - Track lines added and improvements

### AI Assistant Workflow
1. **Ask Questions** - Chat about data, code, or platform
2. **Quick Actions** - One-click analysis and expansion
3. **Get Insights** - AI-powered recommendations
4. **Monitor Progress** - Real-time platform statistics

## 🎨 Theme & Styling

### Color Palette
- **Primary**: Electric Purple (#8B5CF6)
- **Secondary**: Neon Pink (#EC4899)
- **Success**: Emerald Green (#10B981)
- **Warning**: Amber (#F59E0B)
- **Error**: Red (#EF4444)
- **Background**: Dark (#0A0A0A, #1A1A1A)
- **Text**: Light Gray (#E5E7EB, #9CA3AF)

### Design Features
- **Gradient Backgrounds** - Space-like visual effects
- **Glowing Borders** - Interactive element highlights
- **Smooth Animations** - Professional transitions
- **Responsive Layout** - Works on all screen sizes
- **Accessibility** - ARIA labels and keyboard navigation

## 🔧 Development

### Backend Development
```bash
# Run with debug mode
python app.py

# Install development dependencies
pip install -r requirements.txt
```

### Frontend Development
```bash
# Start development server
npm start --prefix frontend

# Build for production
npm run build --prefix frontend

# Run tests
npm test --prefix frontend
```

### Code Structure
- **Modular Components** - Reusable React components
- **Context API** - Centralized state management
- **Service Layer** - Clean API communication
- **Error Handling** - Comprehensive error management
- **Type Safety** - PropTypes validation

## 🚀 Deployment

### Production Build
```bash
# Build frontend
npm run build --prefix frontend

# Start production server
python app.py
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Guidelines
- **Clean Code** - Follow PEP 8 and ESLint standards
- **Modular Design** - Create reusable components
- **Error Handling** - Comprehensive try-catch blocks
- **Documentation** - Clear comments and README updates
- **Testing** - Unit tests for critical functions

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Material-UI** - Beautiful React components
- **Flask** - Lightweight Python web framework
- **React** - Declarative UI library
- **Free AI Simulation** - Local AI processing without external APIs

## 📞 Support

- **Issues**: Report bugs and feature requests
- **Discussions**: Ask questions and share ideas
- **Documentation**: Comprehensive guides and examples
- **Community**: Join our development community

---

**Moduro AI Platform** - Where AI meets modular development, completely free and self-contained. 🚀 