# RSA Algorithm
from decimal import Decimal 

def gcd(a,b): 
	if b==0: 
		return a 
	else: 
		return gcd(b,a%b) 
p = int(input('Enter the value of p = ')) 
q = int(input('Enter the value of q = ')) 
no = int(input('Enter the value of text = ')) 
n = p*q 
t = (p-1)*(q-1) 

for e in range(2,t): 
	if gcd(e,t)== 1: 
		break


for i in range(1,10): 
	x = 1 + i*t 
	if x % e == 0: 
		d = int(x/e) 
		break
ctt = Decimal(0) 
ctt =pow(no,e) 
ct = ctt % n 

dtt = Decimal(0) 
dtt = pow(ct,d) 
dt = dtt % n 

print('n = '+str(n)+' e = '+str(e)+' t = '+str(t)+' d = '+str(d)+' cipher text = '+str(ct)+' decrypted text = '+str(dt)) 



#Diffie-Hellman algorithm

/* This program calculates the Key for two persons 
using the Diffie-Hellman Key exchange algorithm */
#include<stdio.h> 
#include<math.h> 

// Power function to return value of a ^ b mod P 
long long int power(long long int a, long long int b, 
									long long int P) 
{ 
	if (b == 1) 
		return a; 

	else
		return (((long long int)pow(a, b)) % P); 
} 

//Driver program 
int main() 
{ 
	long long int P, G, x, a, y, b, ka, kb; 
	
	// Both the persons will be agreed upon the 
		// public keys G and P 
	P = 23; // A prime number P is taken 
	printf("The value of P : %lld\n", P); 

	G = 9; // A primitve root for P, G is taken 
	printf("The value of G : %lld\n\n", G); 

	// Alice will choose the private key a 
	a = 4; // a is the chosen private key 
	printf("The private key a for Alice : %lld\n", a); 
	x = power(G, a, P); // gets the generated key 
	
	// Bob will choose the private key b 
	b = 3; // b is the chosen private key 
	printf("The private key b for Bob : %lld\n\n", b); 
	y = power(G, b, P); // gets the generated key 

	// Generating the secret key after the exchange 
		// of keys 
	ka = power(y, a, P); // Secret key for Alice 
	kb = power(x, b, P); // Secret key for Bob 
	
	printf("Secret key for the Alice is : %lld\n", ka); 
	printf("Secret Key for the Bob is : %lld\n", kb); 
	
	return 0; 
} 
