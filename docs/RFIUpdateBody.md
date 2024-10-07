# RFIUpdateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rfi** | [**RFIUpdateBodyRfi**](RFIUpdateBodyRfi.md) |  | 

## Example

```python
from procore_sdk.models.rfi_update_body import RFIUpdateBody

# TODO update the JSON string below
json = "{}"
# create an instance of RFIUpdateBody from a JSON string
rfi_update_body_instance = RFIUpdateBody.from_json(json)
# print the JSON string representation of the object
print(RFIUpdateBody.to_json())

# convert the object into a dict
rfi_update_body_dict = rfi_update_body_instance.to_dict()
# create an instance of RFIUpdateBody from a dict
rfi_update_body_from_dict = RFIUpdateBody.from_dict(rfi_update_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


