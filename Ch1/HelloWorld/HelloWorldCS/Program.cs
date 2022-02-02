// Code example file for Python for the C# Developer LinkedIn Learning Course by Joe Marini
using System;

namespace HelloWorldCS
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Console.WriteLine("What is your name? ");
            string str = Console.ReadLine();
            Console.WriteLine("Hello, {0}!", str);
        }
    }
}
