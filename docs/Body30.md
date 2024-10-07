# Body30


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | The company identifier the project is associated with. | 
**project** | [**Project2**](Project2.md) |  | 

## Example

```python
from procore_sdk.models.body30 import Body30

# TODO update the JSON string below
json = "{}"
# create an instance of Body30 from a JSON string
body30_instance = Body30.from_json(json)
# print the JSON string representation of the object
print(Body30.to_json())

# convert the object into a dict
body30_dict = body30_instance.to_dict()
# create an instance of Body30 from a dict
body30_from_dict = Body30.from_dict(body30_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


