# Image1

At least one attribute is required even when an 'upload_uuid' key is provided. If an 'upload_uuid' is not provided above, then the 'data' key must be provided

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private** | **bool** | The Private status of the Image. Defaults to a project configuration. | [optional] 
**provider_type** | **str** | Provider type. Currently supports only &#x60;MarkupLayer&#x60;, and should only be used when adding an Image to markup. | [optional] 
**provider_id** | **int** | Provider ID. Currently supports only MarkupLayer IDs, and should only be used when adding an Image to markup. | [optional] 
**data** | **bytearray** | File to use as image data. Note that it&#39;s only possible to post a file using a multipart/form-data body (see RFC 2388). Most HTTP libraries will do the right thing when you pass in an open file or IO stream. Alternatively you can use an upload_uuid (see Company Uploads or Project Uploads). You should not use both file and upload_uuid fields in the same request. | [optional] 
**source** | **str** | Image source | [optional] 
**description** | **str** | Image description | [optional] 
**image_category_id** | **int** | Image Category ID | [optional] 
**location_id** | **int** | If you want to use an existing location and you have the ID of that existing location use this. &#x60;location_id&#x60; takes precedence over &#x60;mt_location&#x60; | [optional] 
**mt_location** | **List[str]** | Use this for creating a new multi-tier or single-tier Location. This will be ignored if &#x60;location_id&#x60; is provided. | [optional] 
**trade_ids** | **List[int]** | An array of IDs of the Trades of the Image | [optional] 
**log_date** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.image1 import Image1

# TODO update the JSON string below
json = "{}"
# create an instance of Image1 from a JSON string
image1_instance = Image1.from_json(json)
# print the JSON string representation of the object
print(Image1.to_json())

# convert the object into a dict
image1_dict = image1_instance.to_dict()
# create an instance of Image1 from a dict
image1_from_dict = Image1.from_dict(image1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


