#!/usr/bin/env python3
"""
Gamma Coherence Calculator Γ-12
Cálculo determinista de coherencia φ^(-7)
"""
import hashlib
import math
import json
import sys
from datetime import datetime

PHI = (1 + math.sqrt(5)) / 2
PHI_7 = PHI ** (-7)

def calculate_phi_coherence(commit_hash, semantic_score):
    """Calcula coherencia Γ de un commit"""
    hash_int = int(commit_hash[:16], 16)
    hash_normalized = (hash_int % 10000) / 10000
    phi_deviation = abs(hash_normalized - PHI_7)
    
    coherence = (
        0.4 * semantic_score +
        0.3 * (1 - phi_deviation) +
        0.3 * hash_normalized
    )
    return coherence

def generate_gamma_signature(commit_hash, coherence, timestamp=None):
    """Genera firma Gamma criptográfica"""
    ts = timestamp or datetime.now().isoformat()
    sig_data = f"{commit_hash}_{coherence:.5f}_{ts}"
    sig_hash = hashlib.sha256(sig_data.encode()).hexdigest()
    return f"Γ_{sig_hash[:12]}_{coherence:.5f}"

def analyze_commit_message(message):
    """Análisis semántico simple del mensaje"""
    gamma_keywords = ['gamma', 'phi', 'coherence', 'biocrystal', 'dimensional']
    words = message.lower().split()
    
    # Scoring básico
    keyword_score = sum(1 for w in words if any(kw in w for kw in gamma_keywords))
    length_score = min(len(words) / 20, 1.0)
    
    semantic_score = (keyword_score * 0.3 + length_score * 0.7) * 0.8
    return max(min(semantic_score, 1.0), 0.1)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        # Modo: proceso de commit específico
        commit_hash = sys.argv[1]
        message = sys.argv[2]
        
        semantic = analyze_commit_message(message)
        coherence = calculate_phi_coherence(commit_hash, semantic)
        signature = generate_gamma_signature(commit_hash, coherence)
        
        result = {
            "commit_hash": commit_hash,
            "coherence": coherence,
            "signature": signature,
            "coherent": coherence >= PHI_7,
            "phi_threshold": PHI_7,
            "semantic_score": semantic
        }
        
        print(json.dumps(result))
    else:
        # Modo: test básico
        test_hash = hashlib.sha256(b"gamma-test").hexdigest()
        test_msg = "Deploy gamma coherence system"
        
        semantic = analyze_commit_message(test_msg)
        coherence = calculate_phi_coherence(test_hash, semantic)
        signature = generate_gamma_signature(test_hash, coherence)
        
        print(f"🜂 Gamma Coherence Calculator Γ-12")
        print(f"φ^(-7) = {PHI_7:.14f}")
        print(f"Test Hash: {test_hash[:16]}")
        print(f"Message: {test_msg}")
        print(f"Semantic: {semantic:.3f}")
        print(f"Coherence: {coherence:.5f}")
        print(f"Signature: {signature}")
        print(f"Status: {'✅ COHERENTE' if coherence >= PHI_7 else '❌ INCOHERENTE'}")
