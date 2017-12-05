// Advent of Code 2017
// December 05, challenge 1
// takes a list of "jump" to go 
// up and down the list, counting the 
// jumps required to end outside the list

// BOTH GOLD STARS GOT
// this one was too easy
// this is currently a solution for part 2

import java.io.*;
import java.util.*;

public class Jumps {

	public static void main(String[] args) throws Exception {
		// load file
		BufferedReader file = new BufferedReader(new FileReader("input.txt"));

		// build an array
		ArrayList<Integer> jumpList = new ArrayList<Integer>();	
		String line;
		while ( (line = file.readLine() ) != null ) {
			jumpList.add( Integer.parseInt(line) );
		}
		Integer[] jumpArray = jumpList.toArray(new Integer[jumpList.size()]);

		// start jumpy loop
		int i = 0;
		int jumpcount = 0;
		while(i < jumpArray.length ) {
			// get jump to make
			int jump = jumpArray[i];

			// increment the field last got
			if (jump >= 3) {
				jumpArray[i] -= 1;
			} else {
				jumpArray[i] += 1;
			}

			// then do the jump by incrementing index
			i += jump;

			// and count the jump done
			jumpcount++;
		}
		// now it's outside the list
		// print results
		System.out.println("Landed outside list in "+jumpcount+" jumps.");

	} // main
}
