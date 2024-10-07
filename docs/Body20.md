# Body20


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Project ID | 
**commitment_id** | **int** | Commitment ID | 
**requisition** | [**RequisitionSubcontractorInvoice1**](RequisitionSubcontractorInvoice1.md) |  | [optional] 

## Example

```python
from procore_sdk.models.body20 import Body20

# TODO update the JSON string below
json = "{}"
# create an instance of Body20 from a JSON string
body20_instance = Body20.from_json(json)
# print the JSON string representation of the object
print(Body20.to_json())

# convert the object into a dict
body20_dict = body20_instance.to_dict()
# create an instance of Body20 from a dict
body20_from_dict = Body20.from_dict(body20_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


