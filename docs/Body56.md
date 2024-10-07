# Body56


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the Observation Item belongs to | 
**observation** | [**Observation2**](Observation2.md) |  | 

## Example

```python
from procore_sdk.models.body56 import Body56

# TODO update the JSON string below
json = "{}"
# create an instance of Body56 from a JSON string
body56_instance = Body56.from_json(json)
# print the JSON string representation of the object
print(Body56.to_json())

# convert the object into a dict
body56_dict = body56_instance.to_dict()
# create an instance of Body56 from a dict
body56_from_dict = Body56.from_dict(body56_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


