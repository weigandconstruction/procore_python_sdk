# RestV10RfqsIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**contract_id** | **int** | Contract ID | 
**rfq** | [**RFQ3**](RFQ3.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_rfqs_id_patch_request import RestV10RfqsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10RfqsIdPatchRequest from a JSON string
rest_v10_rfqs_id_patch_request_instance = RestV10RfqsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10RfqsIdPatchRequest.to_json())

# convert the object into a dict
rest_v10_rfqs_id_patch_request_dict = rest_v10_rfqs_id_patch_request_instance.to_dict()
# create an instance of RestV10RfqsIdPatchRequest from a dict
rest_v10_rfqs_id_patch_request_from_dict = RestV10RfqsIdPatchRequest.from_dict(rest_v10_rfqs_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


