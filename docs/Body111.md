# Body111


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
from procore_sdk.models.body111 import Body111

# TODO update the JSON string below
json = "{}"
# create an instance of Body111 from a JSON string
body111_instance = Body111.from_json(json)
# print the JSON string representation of the object
print(Body111.to_json())

# convert the object into a dict
body111_dict = body111_instance.to_dict()
# create an instance of Body111 from a dict
body111_from_dict = Body111.from_dict(body111_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


