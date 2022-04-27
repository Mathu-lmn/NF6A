#include<stdio.h>  

void main()  {
	int type_conv=0;
	int sens_conv=0;
	double unit_entered; //double unit_entered was missing ;
	  
//	while (type_conv > 1 || type_conv > 3) { no need for this loop
		printf("What type of conversion do you want to do:  \n 1) Temperature \n 2) Distance \n 3) Weight \n");
		scanf("%d",&type_conv);
/*	}
	while (sens_conv > 1 || sens_conv > 2) { no need for this loop */
		printf("In which direction do you want to do the conversion:\n1) Metric --> Imperial\n 2) Imperial --> Metric \n");
		scanf("%d",&sens_conv); //added the & to point to the variable
//	}
	switch (type_conv) {
		case 1 : printf("Enter the temperature to convert\n"); break; 
		case 2 : printf("Enter the distance to convert\n"); break; 
		case 3 : printf("Enter the weight to convert\n"); break; 
	}
	scanf("%lf",&unit_entered);
	float result; //set the result to float
	switch (type_conv) { //added bracket to initiate the cases and changed the variable in it to select the type of conversion
	case 1 : if (sens_conv=1) result = unit_entered * 9/5 + 32; else result = unit_entered - 32 * 5/9; break;  
	case 2 : if (sens_conv=1) result = unit_entered / 0.30480; else result = unit_entered * 0.30480; break; 
	case 3 : if (sens_conv=1) result = unit_entered * 28.3495; else result = unit_entered / 28.3495; break; 
    } //added closing bracket

	printf("The converted value is: %f \n", result);
//removed the return(0);
}