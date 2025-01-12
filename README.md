# assignment_summarizer
This will create summary from the regulations.txt file

# How to Clone and Install packages Required to Run this project.
### Clone the repository
```
git clone https://github.com/nikeshmangwani/assignment_summarizer.git
```

### Step 01 - Check if Python is Installed if not install please download from 
```
https://www.python.org/downloads/
```
### Step 02 - Navigate to repository
```
cd assignment_summarizer/src
```

### STEP 03- Create a python virtual environment after opening the repository
```
python -m venv summaryenv
```

### Step 04- Activate Python Virtual Environment on Mac/Linux
```
source summaryenv/bin/activate
```

### STEP 05- install the requirements make sure you are under src folder
```
pip install -r requirements.txt
```
# How to Run if all Packages Installed Successfully 
```
python extract_requirements.py
```
# Once Successfully running the .py file check the o/p file src/extracted_requirements.json

```
json

[
    {
        "section_number": "Section 1: Data Privacy and Security",
        "original_text": " Amazon places the highest priority on the protection of customer data and maintaining robust security measures to ensure trust and transparency. The company adheres strictly to global data privacy laws, including the General Data Protection Regulation (GDPR) and the California Consumer Privacy Act (CCPA). All customer data is encrypted both in transit and at rest, utilizing advanced cryptographic methods to prevent unauthorised access. Amazon provides a comprehensive suite of tools for customers to manage their privacy preferences, including options to download, delete, and restrict the use of their personal data. Additionally, Amazon conducts regular security audits and penetration testing to identify and mitigate vulnerabilities. By investing heavily in AI-driven threat detection systems, Amazon ensures that user data remains secure even in the face of evolving cyber threats. The company\u2019s transparency reports outline how data is managed, shared, and protected, offering customers clear insights into Amazon\u2019s commitment to their privacy.",
        "section_summary": "Amazon provides a comprehensive suite of tools for customers to manage their privacy preferences, including options to download, delete, and restrict the use of their personal data.The company\u2019s transparency reports outline how data is managed, shared, and protected, offering customers clear insights into Amazon\u2019s commitment to their privacy."
    },
    {
        "section_number": "Section 2: Consumer Protection",
        "original_text": " Amazon has established robust consumer protection measures to foster trust and ensure a seamless shopping experience. The company\u2019s 30-day return policy is designed to provide customers with sufficient time to evaluate their purchases, ensuring satisfaction and fairness. Amazon\u2019s A-to-Z Guarantee covers the entire purchase process, offering full refunds for items that fail to meet expectations or arrive damaged. To combat counterfeit goods, Amazon has implemented cutting-edge seller verification processes and introduced tools such as Brand Registry and Transparency to empower brands in protecting their intellectual property. Product reviews and ratings undergo rigorous checks to ensure authenticity, preventing fraudulent feedback that could mislead consumers. Dedicated customer service teams are available 24/7 to resolve disputes efficiently, reflecting Amazon\u2019s unwavering commitment to consumer satisfaction.",
        "section_summary": "Amazon\u2019s A-to-Z Guarantee covers the entire purchase process, offering full refunds for items that fail to meet expectations or arrive damaged.Product reviews and ratings undergo rigorous checks to ensure authenticity, preventing fraudulent feedback that could mislead consumers."
    },
    {
        "section_number": "Section 3: Advertising and Marketing Compliance",
        "original_text": " Amazon\u2019s advertising and marketing practices are built upon a foundation of compliance with international standards and local regulations. Advertisements on Amazon\u2019s platform are subject to strict review processes to ensure they are truthful, non-deceptive, and aligned with consumer protection laws. Misleading claims, exaggerated product descriptions, and manipulative marketing tactics are strictly prohibited. To further protect consumers, Amazon enforces rigorous guidelines for influencer marketing, requiring clear disclosure of sponsored content in accordance with FTC guidelines. Advertisements targeting minors are subject to additional scrutiny to ensure ethical compliance and the promotion of age-appropriate content. Regular audits and monitoring of ad campaigns ensure compliance and foster an environment of trust between brands and customers.",
        "section_summary": "Advertisements on Amazon\u2019s platform are subject to strict review processes to ensure they are truthful, non-deceptive, and aligned with consumer protection laws.Regular audits and monitoring of ad campaigns ensure compliance and foster an environment of trust between brands and customers."
    },
    {
        "section_number": "Section 4: Content Moderation and Intellectual Property",
        "original_text": " Amazon takes content moderation and intellectual property protection very seriously. The company\u2019s automated systems and dedicated teams work around the clock to monitor and remove listings that violate its policies. Prohibited items, counterfeit products, and materials infringing intellectual property rights are promptly addressed to ensure a safe and compliant marketplace. Amazon collaborates closely with rights holders through programs such as the Brand Registry and Project Zero, which leverage advanced technology to proactively identify and eliminate counterfeit products. Sellers are educated on compliance with intellectual property laws through detailed guidelines and training resources. In cases where content or listings are removed, Amazon provides a transparent appeal process, allowing sellers to contest decisions and rectify errors efficiently. By continuously refining its policies and leveraging innovative technology, Amazon maintains a marketplace that prioritizes the interests of consumers, sellers, and rights holders alike.",
        "section_summary": "Amazon collaborates closely with rights holders through programs such as the Brand Registry and Project Zero, which leverage advanced technology to proactively identify and eliminate counterfeit products.By continuously refining its policies and leveraging innovative technology, Amazon maintains a marketplace that prioritizes the interests of consumers, sellers, and rights holders alike."
    }
]
```

# Architecture Diagram with Full code Flow along with use of LLM AWS Bedrock Model and Sumy Package

![Code Flow](images/LLM_summarizer)
