# Response2

Response object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Response | 
**corresponding_status** | **str** | Item Status that the Response corresponds to | 

## Example

```python
from procore_sdk.models.response2 import Response2

# TODO update the JSON string below
json = "{}"
# create an instance of Response2 from a JSON string
response2_instance = Response2.from_json(json)
# print the JSON string representation of the object
print(Response2.to_json())

# convert the object into a dict
response2_dict = response2_instance.to_dict()
# create an instance of Response2 from a dict
response2_from_dict = Response2.from_dict(response2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


