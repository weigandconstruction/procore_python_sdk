# ObservationItem1AttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Use :name, :filename to be deprecated | [optional] 
**url** | **str** |  | [optional] 
**thumbnail_url** | **str** | URL | [optional] 
**filename** | **str** | :filename to be deprecated, use :name | [optional] 

## Example

```python
from procore_sdk.models.observation_item1_attachments_inner import ObservationItem1AttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationItem1AttachmentsInner from a JSON string
observation_item1_attachments_inner_instance = ObservationItem1AttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(ObservationItem1AttachmentsInner.to_json())

# convert the object into a dict
observation_item1_attachments_inner_dict = observation_item1_attachments_inner_instance.to_dict()
# create an instance of ObservationItem1AttachmentsInner from a dict
observation_item1_attachments_inner_from_dict = ObservationItem1AttachmentsInner.from_dict(observation_item1_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


