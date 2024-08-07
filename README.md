# RSA-Wiener-Attack

## Overview
This project implements Wiener's attack to exploit a vulnerability in RSA encryption when the private exponent $d$ is relatively small compared to the modulus $N$. The script finds the private key $d$ using continued fractions and then decrypts a given ciphertext. This project demonstrates the potential risks of using small private keys in RSA encryption.

## Features
- **Wiener's Attack**: Uses continued fractions to find the RSA private key $d$ when $d$ is small.
- **RSA Decryption**: Decrypts ciphertext using the discovered private key $d$.
- **Libraries Used**: Utilizes `sympy` for mathematical operations and `contfrac` for continued fractions.

## Detailed Explanation

The code we design in Python exploits a vulnerability in RSA encryption using the Wiener attack, which targets cases where the private key $d$ is relatively small compared to the modulus $N$. The program includes a decryption function and the implementation of the Wiener attack.

### Decryption Function
The decryption function accepts a ciphertext, $N$, and $d$ and decrypts them using the RSA decryption formula, where each part of the ciphertext is raised to the power $d$ and then taken mod $N$ ($m = c^d \mod N$). The results are converted back to characters, reconstructing the original message.

### Wiener Attack Function
The main functionality of the program is found in the `wiener_attack` function, which attempts to find the private key $d$ using the properties of continued fractions. The attack starts by calculating the continued fraction representation of the ratio $e/N$, where $e$ is the public key exponent and $N$ is the modulus. The continued fractions are used to produce convergents, which are simple fractions that approximate $e/N$. Each convergent provides a candidate result for $d$.

Wiener's attack is effective because it exploits the mathematical relationship between $e$, $N$, and $d$ when $d$ is very small. If a valid $d$ is found, it is used to decrypt the ciphertext. If no such $d$ is found, the attack is unsuccessful.

In our case, we successfully find $d$ ($d = 20881$), with the ciphertext decrypting to:
"Just because you are a character doesn't mean that you have character."
You can use different numbers/ciphertexts etc to produce results to your liking.  

For the calculation of continued fractions and convergents, `contfrac.continued_fraction` and `contfrac.convergents` from the contfrac library are used (install with `pip install contfrac`).

## Getting Started

### Prerequisites
- Python 3.x
- SymPy
- contfrac

### Installation
Install the required packages using pip:
```bash
pip install sympy contfrac
