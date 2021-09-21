using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class test : MonoBehaviour
{
    enum Operation 
    {
        // Create
        Move,
        Scale,
        Dye
        // Destory
    }
    
    private static GameObject selectedObject;
    private static Operation operation;

    // Start is called before the first frame update
    void Start()
    {
        Operation operation = Operation.Move;
        selectedObject = GameObject.Find("Cube");
    }


    public void SelectObejct(int val)
    {
        switch (val)
        {
            case 0:
                selectedObject = GameObject.Find("Cube");
                break;
            case 1: 
                selectedObject = GameObject.Find("Sphere");
                break;
            case 2:
                selectedObject = GameObject.Find("Cylinder");
                break;
        }
    }

    public void SelectOperation(int val)
    {
        switch (val)
        {
            case 0: 
                operation = Operation.Move;
                print("Change to Move");
                break;
            case 1: 
                operation = Operation.Scale;            
                print("Change to Scale");
                break;
            case 2:
                operation = Operation.Dye;                
                print("Change to Dye");
                break;
        }
    }

    public void RunOperation()
    {
        switch (operation)
        {
            case Operation.Move:
                print("Move" + selectedObject);
                break;
            case Operation.Scale:
                print("Scale"  + selectedObject);
                break;
            case Operation.Dye:
                print("Dye" + selectedObject);
                break;
        }
    }
}
