# Body28


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**punch_ids** | **List[int]** |  | [optional] 
**recipient** | **str** | Recipient role | [optional] 

## Example

```python
from procore_sdk.models.body28 import Body28

# TODO update the JSON string below
json = "{}"
# create an instance of Body28 from a JSON string
body28_instance = Body28.from_json(json)
# print the JSON string representation of the object
print(Body28.to_json())

# convert the object into a dict
body28_dict = body28_instance.to_dict()
# create an instance of Body28 from a dict
body28_from_dict = Body28.from_dict(body28_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


