# Body69


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the Location belongs to | 
**location** | [**Location3**](Location3.md) |  | 

## Example

```python
from procore_sdk.models.body69 import Body69

# TODO update the JSON string below
json = "{}"
# create an instance of Body69 from a JSON string
body69_instance = Body69.from_json(json)
# print the JSON string representation of the object
print(Body69.to_json())

# convert the object into a dict
body69_dict = body69_instance.to_dict()
# create an instance of Body69 from a dict
body69_from_dict = Body69.from_dict(body69_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


