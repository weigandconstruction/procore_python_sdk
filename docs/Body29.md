# Body29


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Email Subject | [optional] 
**body** | **str** | Email Body | [optional] 
**distribution_ids** | **List[int]** |  | [optional] 
**cc_distribution_ids** | **List[int]** |  | [optional] 
**bcc_distribution_ids** | **List[int]** |  | [optional] 

## Example

```python
from procore_sdk.models.body29 import Body29

# TODO update the JSON string below
json = "{}"
# create an instance of Body29 from a JSON string
body29_instance = Body29.from_json(json)
# print the JSON string representation of the object
print(Body29.to_json())

# convert the object into a dict
body29_dict = body29_instance.to_dict()
# create an instance of Body29 from a dict
body29_from_dict = Body29.from_dict(body29_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


