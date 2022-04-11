#include <stdio.h>

int main() 
{
  float ph;
  scanf("%f", &ph);
  if (ph <= 1.0 | ph >= 14.0)
    return 0;
  
  else if(ph < 7.0)
    printf("Acida\n ");

  else if(ph > 7.0)
    printf("Basica\n ");

  else
    printf("Neutra\n ");
    
  return 0;
}
