/*
	SLongofono     Week 01 Spring 2016     Beginner
	
	Stock Program

	Given a text file of space-delimited stock prices, determine the best
	trade possible under the following restrictions:
		1. You may not buy for a price which occurs after the sale price
		2. You may not sell for a price which occurs before the buy price
		3. At least one tick must have passed before you may sell,
		   i.e. you can't buy a stock and immediately sell it at the next
		   price

	The output should be formatted as a buy price and a sell price
*/

#include <stdio.h>
#define MAX 100

//initiates the price find algorithm, prints results to console
void getPrices(int count, float nums[count]);

//#LILJON  Returns the index of the lowest price above the minimum parameter,
//Returns -1 if no such number exists.
int getLow(int count, float minimum, float nums[count]);

//#COINCIDENCE Returns the index of the highest price above a minimum parameter,
//as found from the index one removed from the position passed in.  Returns
//-1 if there are no higher prices.
int getHigh(int count, int position, float minimum, float nums[count]);

int main(void){

	float prices[MAX];
	int i = 0;
	int count = 0;

	while(1==scanf("%f", &prices[i])){
		count++;
		i++;
	}

	for(i=0; i<count; i++){
		printf("%f ", prices[i]);
	}

	putchar('\n');

	getPrices(count, prices);

	return 0;
}

int getLow(int count, float minimum, float nums[count]){

	int i, pos;
	pos = -1;
	float min = 10000000;
	for(i=0; i<count; i++){

		//check that we're above low bound
		if(nums[i] > minimum){
			
			//check against current minimum
			if(min>nums[i]){
				min = nums[i];
				pos = i;
			}
		} 	
	}
	return pos;
}

int getHigh(int count, int position, float price, float nums[count]){

	int i, pos;
	pos = position;
	float max = price;

	//valid sale prices must be one index removed from buy index param
	for(i = position+2; i<count; i++){
	
		//verify price is greater than buy price
		if(nums[i] > price){

			//check against current maximum
			if (max < nums[i]){
				max = nums[i];
				pos = i;
			}
		}
	}

	//fails if positon didn't change (no price higher than buy)
	if(nums[pos] <= price){
		return -1;
	}
	return pos;
}

void getPrices(int count, float nums[count]){

	float profit = 0;
	int buy = -1;
	int sell = -1;

	int lowPos = getLow(count, 0.0, nums);
	int highPos = getHigh(count, lowPos, nums[lowPos], nums);

	//with valid low end
	while(lowPos>=0){

		//if there is a valid high, proceed, else, get the next lowest
		if(highPos >=0){
			
			//we can make a sale, check profit against highest known
			if((nums[highPos] - nums[lowPos]) > profit){
				buy = lowPos;
				sell = highPos;
				profit = nums[highPos]-nums[lowPos];
			}

			//get new low and high
			lowPos = getLow(count, nums[lowPos], nums);
			highPos = getHigh(count, lowPos, nums[lowPos], nums);
		}
		else{
			lowPos = getLow(count, nums[lowPos], nums);
			highPos = getHigh(count, lowPos, nums[lowPos], nums);
		}
	}

	if(nums[buy]==0 && nums[sell]==0){
		printf("No profitable trades found\n");
	}
	else{
		printf("%.2f %.2f\n", nums[buy], nums[sell]);
	}	
}


