#include <iostream>
using namespace std;

string Encryption(string plain_text, string key)
{
  string result = "";
  int count = 0;
  for (int i = 0; i < plain_text.length(); i++)
  {
    if (count >= key.length())
    {
      count = 0;
    }
    if (isalpha(plain_text[i]))
    {
      if (islower(plain_text[i]))
      
        result +=(((plain_text[i] - 97)+((tolower(key[count])) - 97))%26)+97;
      if (isupper(plain_text[i]))
       
        result +=(((plain_text[i] - 65)+((toupper(key[count])) - 65))%26)+65;
      count++;
    }
    else
    {
      result += plain_text[i];
    }
  }
  return result;
}

string Decryption(string cipher_text, string key)
{
  string result = "";
  int count = 0;
  for (int i = 0; i < cipher_text.length(); i++)
  {
    if (count >= key.length())
    {
      count = 0;
    }
    if (isalpha(cipher_text[i]))
    {
      if (islower(cipher_text[i]))
      
        result +=((((cipher_text[i] - 97)-((tolower(key[count])) - 97))+26)%26)+97;
      if (isupper(cipher_text[i]))
       
        result +=((((cipher_text[i] - 65)-((toupper(key[count])) - 65))+26)%26)+65;
      count++;
    }
    else
    {
      result += cipher_text[i];
    }
  }
  return result;
}
int main()
{
  string plain_text;
  string cipher_text,output_text;
  string key;
  cout << "Enter Plain Text: ";
  getline(cin, plain_text);
  cout << "Enter Key: ";
  cin >> key;
  cipher_text= Encryption(plain_text, key);
  cout<<"Encryption: "<<cipher_text<<endl;
  output_text=Decryption(cipher_text,key);
  cout<<"Decryption: "<<output_text;
}

