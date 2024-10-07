# RFQResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment in response to the latest quote | [optional] 
**prostore_file_ids** | **List[int]** | Prostore file IDs | [optional] 

## Example

```python
from procore_sdk.models.rfq_response1 import RFQResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of RFQResponse1 from a JSON string
rfq_response1_instance = RFQResponse1.from_json(json)
# print the JSON string representation of the object
print(RFQResponse1.to_json())

# convert the object into a dict
rfq_response1_dict = rfq_response1_instance.to_dict()
# create an instance of RFQResponse1 from a dict
rfq_response1_from_dict = RFQResponse1.from_dict(rfq_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


