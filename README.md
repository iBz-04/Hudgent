# Islamic AI Agent System

An AI-powered q & a agent system focused on Islamic knowledge, leveraging scraped content from authentic sources and OpenAI's NLP capabilities. The system provides context-aware answers about Islamic practices, beliefs, and traditions while maintaining source fidelity.

## Preview

<img src="https://res.cloudinary.com/diekemzs9/image/upload/v1741292644/Screenshot_2025-03-06_191123_m0nrti.png" alt="My Image" width="950"/>

## Key Features 

- **Q&A Interface**: Natural language interface for asking Islamic-related questions
- **Context-Aware Answers**: AI responses grounded in verified Islamic content
- **Knowledge Base**:
  - Pre-loaded sample data covering fasting (Oruç), Ramadan, and prayer (Dua)
  - Web crawler integration for [islamveihsan.com](https://www.islamveihsan.com/)
- **Search Index**: Fast content retrieval system using Whoosh search engine
- **Validation System**: Ensures answers stay within provided Islamic context
- **Batch Processing**: Automated setup script for data/index preparation



## Working Principle
The system operates in 3 phases:
1. **Data Preparation**: Creates sample data & crawls a given  websites
2. **Index Building**: Creates searchable knowledge base
3. **Q&A Interface**: Interactive Islamic knowledge assistant

```bash
# Start the system (Windows)
run_project.bat

# Or run manually:
python create_sample_data.py
python indexer/build_index.py
python main.py
```

## Architecture Components 🧠
- `create_sample_data.py`: Creates initial dataset with Islamic rulings
- `indexer/`: Search index builder using Whoosh
- `crawler/`: Website spider for islamveihsan.com
- `main.py`: Core AI response generation
- `config/`: Contains API and website configurations

## Author 

- `Ibrahim` : @iBz-04