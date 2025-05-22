def get_disease_info():
    """
    Returns comprehensive information about skin diseases.
    """
    return {
        'Acne': {
            'description': 'A common skin condition that occurs when hair follicles become plugged with oil and dead skin cells, leading to whiteheads, blackheads, and pimples.',
            'recommendations': [
                'Use gentle, non-comedogenic skincare products',
                'Avoid picking or squeezing pimples',
                'Consider over-the-counter treatments with salicylic acid or benzoyl peroxide',
                'Consult a dermatologist for persistent or severe cases',
                'Maintain a consistent skincare routine'
            ],
            'severity': 'Low to Moderate'
        },
        'Actinic_Keratosis': {
            'description': 'Rough, scaly patches on the skin caused by years of sun exposure. These precancerous lesions can develop into skin cancer if left untreated.',
            'recommendations': [
                'Seek immediate dermatological evaluation',
                'Use broad-spectrum sunscreen daily',
                'Avoid excessive sun exposure',
                'Consider professional treatment options',
                'Monitor for changes in appearance'
            ],
            'severity': 'Moderate to High'
        },
        'Benign_tumors': {
            'description': 'Non-cancerous growths on the skin that do not spread to other parts of the body. While generally harmless, they should be monitored.',
            'recommendations': [
                'Have regular skin examinations',
                'Monitor for changes in size, color, or texture',
                'Consult a dermatologist for proper diagnosis',
                'Consider removal if cosmetically bothersome',
                'Protect from sun exposure'
            ],
            'severity': 'Low'
        },
        'Bullous': {
            'description': 'A group of skin conditions characterized by the formation of blisters filled with fluid. Can be caused by various factors including autoimmune conditions.',
            'recommendations': [
                'Seek immediate medical attention',
                'Do not pop or break blisters',
                'Keep the affected area clean and dry',
                'Follow prescribed treatment regimen',
                'Monitor for signs of infection'
            ],
            'severity': 'Moderate to High'
        },
        'Candidiasis': {
            'description': 'A fungal infection caused by Candida yeast, commonly affecting warm, moist areas of the body such as skin folds.',
            'recommendations': [
                'Keep affected areas clean and dry',
                'Use antifungal medications as prescribed',
                'Wear loose, breathable clothing',
                'Maintain good hygiene',
                'Consult a healthcare provider for persistent infections'
            ],
            'severity': 'Low to Moderate'
        },
        'DrugEruption': {
            'description': 'Skin reactions caused by medications. Can range from mild rashes to severe, life-threatening conditions.',
            'recommendations': [
                'Discontinue suspected medication immediately',
                'Seek emergency medical care if severe',
                'Inform all healthcare providers about drug allergies',
                'Keep a list of medications that cause reactions',
                'Consider allergy testing'
            ],
            'severity': 'Moderate to High'
        },
        'Eczema': {
            'description': 'A chronic inflammatory skin condition characterized by dry, itchy, and inflamed skin. Often associated with allergies and asthma.',
            'recommendations': [
                'Use gentle, fragrance-free moisturizers',
                'Avoid known triggers (certain soaps, fabrics, stress)',
                'Take lukewarm baths and pat skin dry',
                'Use prescribed topical medications',
                'Consider seeing an allergist or dermatologist'
            ],
            'severity': 'Low to Moderate'
        },
        'Infestations_Bites': {
            'description': 'Skin reactions caused by insect bites or parasitic infestations. Can cause itching, redness, and secondary infections.',
            'recommendations': [
                'Identify and eliminate the source of infestation',
                'Use anti-itch treatments to prevent scratching',
                'Keep affected areas clean',
                'Consider antihistamines for allergic reactions',
                'Seek medical care for severe reactions or infections'
            ],
            'severity': 'Low to Moderate'
        },
        'Lichen': {
            'description': 'A group of inflammatory skin conditions that can affect various parts of the body, characterized by distinctive patterns and textures.',
            'recommendations': [
                'Consult a dermatologist for proper diagnosis',
                'Follow prescribed treatment regimen',
                'Avoid scratching affected areas',
                'Use gentle skincare products',
                'Monitor for changes in symptoms'
            ],
            'severity': 'Moderate'
        },
        'Lupus': {
            'description': 'An autoimmune disease that can affect the skin and other organs. Skin manifestations include characteristic rashes, particularly on sun-exposed areas.',
            'recommendations': [
                'Seek immediate medical evaluation',
                'Use high-SPF sunscreen daily',
                'Avoid excessive sun exposure',
                'Follow prescribed treatment plan',
                'Regular monitoring by rheumatologist and dermatologist'
            ],
            'severity': 'High'
        },
        'Moles': {
            'description': 'Common skin growths made up of pigmented cells. Most moles are harmless, but changes should be monitored for signs of skin cancer.',
            'recommendations': [
                'Perform regular self-examinations',
                'Monitor for ABCDE changes (Asymmetry, Border, Color, Diameter, Evolving)',
                'Have annual dermatological skin checks',
                'Protect from sun exposure',
                'Consult a dermatologist for suspicious changes'
            ],
            'severity': 'Low'
        },
        'Psoriasis': {
            'description': 'A chronic autoimmune condition that causes rapid skin cell turnover, resulting in thick, scaly patches on the skin.',
            'recommendations': [
                'Consult a dermatologist for treatment options',
                'Use prescribed topical treatments',
                'Consider phototherapy or systemic treatments for severe cases',
                'Maintain skin hydration',
                'Manage stress levels'
            ],
            'severity': 'Moderate'
        },
        'Rosacea': {
            'description': 'A chronic inflammatory skin condition that primarily affects the face, causing redness, visible blood vessels, and sometimes acne-like bumps.',
            'recommendations': [
                'Identify and avoid personal triggers',
                'Use gentle, fragrance-free skincare products',
                'Apply broad-spectrum sunscreen daily',
                'Consider prescription treatments',
                'Avoid harsh scrubbing or irritating products'
            ],
            'severity': 'Low to Moderate'
        },
        'Seborrh_Keratoses': {
            'description': 'Common, non-cancerous skin growths that appear as waxy, scaly, or warty patches. More common with aging.',
            'recommendations': [
                'Have regular skin examinations',
                'Monitor for changes in appearance',
                'Consider removal if cosmetically bothersome or irritated',
                'Distinguish from more serious skin conditions',
                'Protect from sun exposure'
            ],
            'severity': 'Low'
        },
        'SkinCancer': {
            'description': 'Malignant growth of skin cells that can spread to other parts of the body if not treated promptly. Requires immediate medical attention.',
            'recommendations': [
                'Seek immediate dermatological evaluation',
                'Follow up with oncology if confirmed',
                'Consider surgical removal or other treatments',
                'Regular monitoring and follow-up care',
                'Strict sun protection measures'
            ],
            'severity': 'High - Medical Emergency'
        },
        'Sun_Sunlight_Damage': {
            'description': 'Skin damage caused by prolonged exposure to ultraviolet radiation, including sun spots, wrinkles, and increased cancer risk.',
            'recommendations': [
                'Use broad-spectrum sunscreen daily (SPF 30+)',
                'Avoid peak sun hours (10 AM - 4 PM)',
                'Wear protective clothing and hats',
                'Consider professional treatments for existing damage',
                'Regular dermatological check-ups'
            ],
            'severity': 'Low to Moderate'
        },
        'Tinea': {
            'description': 'Fungal infections of the skin, hair, or nails caused by dermatophytes. Includes conditions like ringworm, athlete\'s foot, and jock itch.',
            'recommendations': [
                'Use antifungal medications as prescribed',
                'Keep affected areas clean and dry',
                'Avoid sharing personal items',
                'Wear breathable clothing and shoes',
                'Complete full course of treatment'
            ],
            'severity': 'Low to Moderate'
        },
        'Unknown_Normal': {
            'description': 'Skin appears normal or the condition is not clearly identifiable. This may represent healthy skin or require further evaluation.',
            'recommendations': [
                'Continue regular skin self-examinations',
                'Maintain good skincare routine',
                'Protect skin from sun damage',
                'Consult a dermatologist if concerns develop',
                'Follow general skin health guidelines'
            ],
            'severity': 'Low'
        },
        'Vascular_Tumors': {
            'description': 'Growths composed of blood vessels that can appear as red or purple marks on the skin. Most are benign but should be evaluated.',
            'recommendations': [
                'Consult a dermatologist for proper diagnosis',
                'Monitor for changes in size or appearance',
                'Consider treatment if cosmetically concerning',
                'Protect from trauma and injury',
                'Regular follow-up as recommended'
            ],
            'severity': 'Low to Moderate'
        },
        'Vasculitis': {
            'description': 'Inflammation of blood vessels that can affect the skin, causing various rashes, ulcers, or nodules. Can be part of systemic disease.',
            'recommendations': [
                'Seek immediate medical evaluation',
                'May require systemic treatment',
                'Monitor for systemic symptoms',
                'Follow prescribed treatment regimen',
                'Regular follow-up with rheumatologist or dermatologist'
            ],
            'severity': 'Moderate to High'
        },
        'Vitiligo': {
            'description': 'An autoimmune condition that causes loss of skin pigmentation, resulting in white patches on the skin.',
            'recommendations': [
                'Consult a dermatologist for treatment options',
                'Use high-SPF sunscreen on affected areas',
                'Consider topical treatments or phototherapy',
                'Provide emotional support as needed',
                'Join support groups if helpful'
            ],
            'severity': 'Low to Moderate'
        },
        'Warts': {
            'description': 'Common viral infections of the skin caused by human papillomavirus (HPV), appearing as rough, raised growths.',
            'recommendations': [
                'Consider over-the-counter treatments first',
                'Consult healthcare provider for persistent warts',
                'Avoid picking or scratching',
                'Prevent spreading to others',
                'Boost immune system through healthy lifestyle'
            ],
            'severity': 'Low'
        }
    }