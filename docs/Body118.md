# Body118


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**budget_line_item** | [**BudgetLineItem2**](BudgetLineItem2.md) |  | 

## Example

```python
from procore_sdk.models.body118 import Body118

# TODO update the JSON string below
json = "{}"
# create an instance of Body118 from a JSON string
body118_instance = Body118.from_json(json)
# print the JSON string representation of the object
print(Body118.to_json())

# convert the object into a dict
body118_dict = body118_instance.to_dict()
# create an instance of Body118 from a dict
body118_from_dict = Body118.from_dict(body118_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


