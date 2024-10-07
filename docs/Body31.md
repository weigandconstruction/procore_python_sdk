# Body31


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | The unique identifier for the Company the Project is associated with. | 
**project** | [**Project5**](Project5.md) |  | 

## Example

```python
from procore_sdk.models.body31 import Body31

# TODO update the JSON string below
json = "{}"
# create an instance of Body31 from a JSON string
body31_instance = Body31.from_json(json)
# print the JSON string representation of the object
print(Body31.to_json())

# convert the object into a dict
body31_dict = body31_instance.to_dict()
# create an instance of Body31 from a dict
body31_from_dict = Body31.from_dict(body31_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


