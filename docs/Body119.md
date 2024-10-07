# Body119


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**budget_line_item** | [**BudgetLineItem3**](BudgetLineItem3.md) |  | 

## Example

```python
from procore_sdk.models.body119 import Body119

# TODO update the JSON string below
json = "{}"
# create an instance of Body119 from a JSON string
body119_instance = Body119.from_json(json)
# print the JSON string representation of the object
print(Body119.to_json())

# convert the object into a dict
body119_dict = body119_instance.to_dict()
# create an instance of Body119 from a dict
body119_from_dict = Body119.from_dict(body119_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


