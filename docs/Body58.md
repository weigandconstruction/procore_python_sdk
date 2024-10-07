# Body58


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
from procore_sdk.models.body58 import Body58

# TODO update the JSON string below
json = "{}"
# create an instance of Body58 from a JSON string
body58_instance = Body58.from_json(json)
# print the JSON string representation of the object
print(Body58.to_json())

# convert the object into a dict
body58_dict = body58_instance.to_dict()
# create an instance of Body58 from a dict
body58_from_dict = Body58.from_dict(body58_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


