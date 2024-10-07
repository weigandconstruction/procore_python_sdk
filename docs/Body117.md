# Body117


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**budget_line_item** | [**BudgetLineItem1**](BudgetLineItem1.md) |  | 

## Example

```python
from procore_sdk.models.body117 import Body117

# TODO update the JSON string below
json = "{}"
# create an instance of Body117 from a JSON string
body117_instance = Body117.from_json(json)
# print the JSON string representation of the object
print(Body117.to_json())

# convert the object into a dict
body117_dict = body117_instance.to_dict()
# create an instance of Body117 from a dict
body117_from_dict = Body117.from_dict(body117_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


