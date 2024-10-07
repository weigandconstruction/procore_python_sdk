# Body19


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Project ID | 
**commitment_id** | **int** | Commitment ID | 
**requisition** | [**RequisitionSubcontractorInvoice**](RequisitionSubcontractorInvoice.md) |  | [optional] 

## Example

```python
from procore_sdk.models.body19 import Body19

# TODO update the JSON string below
json = "{}"
# create an instance of Body19 from a JSON string
body19_instance = Body19.from_json(json)
# print the JSON string representation of the object
print(Body19.to_json())

# convert the object into a dict
body19_dict = body19_instance.to_dict()
# create an instance of Body19 from a dict
body19_from_dict = Body19.from_dict(body19_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


