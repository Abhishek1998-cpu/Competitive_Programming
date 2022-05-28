function subArray(n)
{
     
    // Pick starting point
    for(let i = 0; i < n; i++)
    {
          
        // Pick ending point
        for(let j = i; j < n; j++)
        {
             
            // Print subarray between current
            // starting and ending points
            for(let k = i; k <= j; k++)
                document.write(arr[k] + " ");
                 
              document.write("</br>");
        }
    }
}