# Body70


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the Location belongs to | 
**location** | [**Location4**](Location4.md) |  | 

## Example

```python
from procore_sdk.models.body70 import Body70

# TODO update the JSON string below
json = "{}"
# create an instance of Body70 from a JSON string
body70_instance = Body70.from_json(json)
# print the JSON string representation of the object
print(Body70.to_json())

# convert the object into a dict
body70_dict = body70_instance.to_dict()
# create an instance of Body70 from a dict
body70_from_dict = Body70.from_dict(body70_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


