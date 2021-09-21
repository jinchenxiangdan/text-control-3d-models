using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class chat : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        // logo and check all objects
        // all selectable objects are taged with "3d_object"
        print("Hello, Welcome to TextContrlScene!");
        GameObject[] allObjects = GameObject.FindGameObjectsWithTag("3d_object");
        foreach(GameObject obj in allObjects)
            print("Objects: " + obj);
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    // functions to test idea and code
    public void MoveToStage(GameObject obj)
    {
        Vector3 targetPosition = new Vector3(300f, 250f, 10f);
        Transform objTransform = obj.GetComponent<Transform>();
        print(objTransform.position);
        obj.transform.position = targetPosition;
    }

    public void ExchangePositionWithObjectOnStage(GameObject obj)
    {

    }
}
