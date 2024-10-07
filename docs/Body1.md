# Body1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**updates** | [**List[WorkOrderContract1]**](WorkOrderContract1.md) | Updated Work order contracts | 

## Example

```python
from procore_sdk.models.body1 import Body1

# TODO update the JSON string below
json = "{}"
# create an instance of Body1 from a JSON string
body1_instance = Body1.from_json(json)
# print the JSON string representation of the object
print(Body1.to_json())

# convert the object into a dict
body1_dict = body1_instance.to_dict()
# create an instance of Body1 from a dict
body1_from_dict = Body1.from_dict(body1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


