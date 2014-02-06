#include <stdio.h>
#include <stdlib.h>

int main(int argn, char * argc[])
{
	unsigned int width = 909, depth = 298, pedding, width_with_pedding;
	unsigned int boat, sign;
	int i,j,count;
	FILE *fp_in, *fp_out;
	fp_in = fopen("grid_bits.txt","r");
	fp_out = fopen("map.dat","wb");

	pedding = (32 - width & 31) & 31;
	width_with_pedding = width + pedding;
	fwrite(&width_with_pedding,sizeof(width),1,fp_out);
	fwrite(&depth,sizeof(depth),1,fp_out);

	for (j = 0; j < depth; j++)
	{
		boat = 0;
		count = 0;
		for (i = 0; i < width; i++)
		{
			fscanf(fp_in, "%u", &sign);
			boat <<= 1;
			boat |= sign;
			count++;
			if (count == 32) {
				fwrite(&boat, sizeof(boat), 1, fp_out);
				count = boat = 0;
			}
		}
		if (pedding) 
		{
			boat <<= pedding;
			fwrite(&boat, sizeof(boat), 1, fp_out);
		}
	}
	fclose(fp_in);
	fclose(fp_out);
}
