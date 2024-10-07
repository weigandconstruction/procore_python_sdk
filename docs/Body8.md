# Body8


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updates** | [**List[UnitOfMeasureToSync]**](UnitOfMeasureToSync.md) |  | 
**deletes** | **List[int]** |  | [optional] 

## Example

```python
from procore_sdk.models.body8 import Body8

# TODO update the JSON string below
json = "{}"
# create an instance of Body8 from a JSON string
body8_instance = Body8.from_json(json)
# print the JSON string representation of the object
print(Body8.to_json())

# convert the object into a dict
body8_dict = body8_instance.to_dict()
# create an instance of Body8 from a dict
body8_from_dict = Body8.from_dict(body8_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


