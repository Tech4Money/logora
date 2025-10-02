# Overview

Logora is an AI-powered coding agent that uses a reasoning-first approach to break down coding requests into logical subtasks and generate code for each. The application leverages OpenAI's GPT-4 to intelligently decompose user requests into 4-5 actionable subtasks, then generates relevant code for each step. Built with Flask, it provides a web interface for users to submit coding requests and view structured, formatted results.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture

**Technology Stack**: Pure HTML/CSS with embedded styling in templates

**Design Pattern**: Server-side rendering with Jinja2 templates
- Templates are served directly from Flask routes
- Minimal JavaScript for form submission and dynamic content updates
- Gradient-based UI design (purple/violet theme) for modern aesthetic
- Responsive design using CSS flexbox/grid patterns

**Rationale**: Chose server-side rendering over a separate frontend framework to keep the application simple and reduce complexity. This approach minimizes dependencies and makes the codebase easier to maintain for a single-page application.

## Backend Architecture

**Technology Stack**: Python Flask web framework

**Design Pattern**: Lightweight microservice architecture
- Single Flask application (`app.py`) serves as the main entry point
- Modular function design for AI interactions (`hrm_plan` for task decomposition)
- Environment-based configuration using python-dotenv
- RESTful API endpoints for handling user requests

**Rationale**: Flask provides flexibility and simplicity for rapid development. The modular function approach allows easy extension of AI capabilities without restructuring the entire application.

## AI Integration

**Model**: OpenAI GPT-4o-mini for task decomposition

**Architecture Decision**: Two-phase AI reasoning approach
1. **Planning Phase**: `hrm_plan()` function breaks down user requests into subtasks using structured prompts
2. **Code Generation Phase**: (Implementation appears incomplete in provided files)

**Prompt Engineering Strategy**:
- System role defines AI as "expert software architect"
- Explicit instructions to return 4-5 specific, actionable subtasks
- Temperature set to 0.7 for balanced creativity and consistency
- Token limit of 500 for concise responses

**Rationale**: The reasoning-first approach ensures generated code is well-structured and logically organized. Breaking tasks into subtasks allows for more precise code generation and better tracking of progress.

## Configuration Management

**Pattern**: Environment variables with fallback defaults
- API keys stored in `.env` file (excluded from version control)
- Session secrets with development fallbacks
- `.env.example` template provided for easy setup

**Rationale**: Separates sensitive configuration from code, enabling secure deployment across different environments while maintaining developer convenience.

## Error Handling

**Strategy**: Defensive programming with validation checks
- OpenAI client initialization validates API key presence
- Try-catch blocks in AI interaction functions (partial implementation visible)
- Graceful error messaging to users

**Rationale**: Prevents application crashes from configuration issues or API failures, providing better user experience.

# External Dependencies

## Third-Party APIs

**OpenAI API** (Primary Integration)
- **Purpose**: Powers AI reasoning and code generation capabilities
- **Model**: GPT-4o-mini for cost-effective task decomposition
- **Authentication**: API key-based authentication via environment variables
- **Usage Pattern**: Chat completions API for conversational AI interactions
- **Configuration**: Adjustable temperature (0.7) and max tokens (500) for balanced output

## Python Packages

**Flask** (Web Framework)
- **Purpose**: HTTP server, routing, template rendering
- **Features Used**: Route handlers, Jinja2 templating, request/response handling, session management

**openai** (Official OpenAI Python Client)
- **Purpose**: Interface with OpenAI's GPT models
- **Version**: Latest (as specified in requirements.txt)

**python-dotenv** (Configuration Management)
- **Purpose**: Load environment variables from `.env` file
- **Usage**: Securely manage API keys and secrets

## Potential Future Dependencies

Based on the application's architecture, future enhancements may require:
- **Database**: SQLite/PostgreSQL for storing user requests and generated code history
- **Caching**: Redis for caching AI responses to reduce API costs
- **Authentication**: Flask-Login or similar for user management
- **Code Formatting**: Black or autopep8 for formatting generated code
- **Syntax Highlighting**: Pygments for enhanced code display