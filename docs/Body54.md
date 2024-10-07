# Body54


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the Observation Item belongs to | 
**attachments** | **List[str]** | Observation Item Attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 
**inspection_item_failed** | **int** | 1 denotes that this Observation Item is being created from a failed Checklist Item. This will update the status of the Checklist Item to &#39;no&#39; (fail). &#x60;observation[checklist_item_id]&#x60; must be provided for this to work. | [optional] 
**observation** | [**Observation**](Observation.md) |  | 

## Example

```python
from procore_sdk.models.body54 import Body54

# TODO update the JSON string below
json = "{}"
# create an instance of Body54 from a JSON string
body54_instance = Body54.from_json(json)
# print the JSON string representation of the object
print(Body54.to_json())

# convert the object into a dict
body54_dict = body54_instance.to_dict()
# create an instance of Body54 from a dict
body54_from_dict = Body54.from_dict(body54_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


